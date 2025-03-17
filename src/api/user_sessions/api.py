from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserSession
from websites.models import WebsiteGroup
from .serializers import UserSessionBriefSerializer,CreateUserSessionSerializer, UserSessionWithWebsitesGroup
from websites.serializers import WebsiteStatusSerializer
from django.db.models import Count
import csv
from django.http import StreamingHttpResponse

def string_to_bool(value):
      return value.lower() in ('true', '1', 'yes') 

def get_user_sessions_by_filters(query_params):
   filters = {}
   if query_params.get('follow_up_group', None)  is not None:
      filters['follow_up_group__isnull'] = not string_to_bool(query_params.get('follow_up_group'))
   if query_params.get('repeated', None) is not None and not string_to_bool(query_params.get('repeated')):
      unique_emails = UserSession.objects.filter(**filters).values('email').distinct()
      filters['email__in'] = [email['email'] for email in unique_emails if UserSession.objects.filter(email=email['email']).count() == 1]
   return UserSession.objects.filter(**filters)

class GetUserSessionsAPI(APIView):

   def get(self, request):
      return Response(UserSessionWithWebsitesGroup(get_user_sessions_by_filters(request.GET), many=True).data)

class CreateUserSessionAPI(APIView):

    def post(self, request):
        user_session_serializer = CreateUserSessionSerializer(data=request.data)
        if (not user_session_serializer.is_valid()):
            return Response(user_session_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_session = UserSession.objects.create(**user_session_serializer.validated_data)

        # assign a website group to the user session
        website_groups = WebsiteGroup.objects.annotate(sessions_count=Count('user_sessions')).order_by('sessions_count', 'order')
        user_session.website_group = website_groups[0]
        user_session.save()
        return Response(UserSessionBriefSerializer(user_session).data, status=status.HTTP_201_CREATED)


class GetUserSessionAPI(APIView):
    def get(self, request, id):
      return Response(UserSessionWithWebsitesGroup(UserSession.objects.get(pk=id)).data)

class DeleteUserSessionAPI(APIView):

   def delete(self, request, id):
      return Response(UserSession.objects.get(pk=id).delete())
   

class GetUserSessionWebsitesStatusAPI(APIView):
   
   def get(self, request, user_session_id):
      user_session = UserSession.objects.get(pk=user_session_id)
      def add_status(website):
         website.completed = user_session.samples.filter(website=website).exists()
         return website
      if (user_session.follow_up_group):
         target_group = user_session.follow_up_group
      else:
         target_group = user_session.website_group
      websites = map(add_status, target_group.get_websites_by_order())
      return Response(WebsiteStatusSerializer(websites,many=True).data)
   
class AssignFollowUpToUserSessionAPI(APIView):
   
   def put(self, request):
      for assignment in request.data['assignments']:
         user_session = UserSession.objects.get(pk=assignment['user_session_id'])
         if (user_session.website_group.id == assignment['follow_up_group_id']):
            return Response({'error': 'No se puede asignar el mismo grupo'}, status=status.HTTP_400_BAD_REQUEST)
         user_session.follow_up_group_id = assignment['follow_up_group_id']
         user_session.save()
      return Response({'success': 'Follow-up asignados correctamente'})

class Echo:
    def write(self, value):
        return value

class ExportUserSessionsAPI(APIView):

   def get(self, request):
      referer = request.META.get('HTTP_REFERER', 'No referer')
      def format_row(session):
        return [
            session.id,
            session.website_group.name,
            session.email,
            session.country, 
            session.age,
            session.gender,
            session.purchases,
            session.date,
            session.follow_up_group.name if session.follow_up_group else "No asignado",
            referer + "start?sessionId=" + str(session.id)
        ]
      
      pseudo_buffer = Echo()
      writer = csv.writer(pseudo_buffer)
      rows = list(map(format_row, get_user_sessions_by_filters(request.GET)))
      header = [["id", "website_group", "email", "country", "age", "gender", "purchases", "date", "follow_up", "link"]]
      return StreamingHttpResponse(
        (writer.writerow(row) for row in (header + rows)),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="usuarios.csv"'})
