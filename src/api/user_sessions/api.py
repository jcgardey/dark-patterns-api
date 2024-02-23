from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserSession
from websites.models import WebsiteGroup
from .serializers import UserSessionBriefSerializer, UserSessionFullSerializer
from websites.serializers import WebsiteStatusSerializer
from django.db.models import Count

class GetUserSessionsAPI(APIView):
    def get(self, request):
      return Response(UserSessionBriefSerializer(UserSession.objects.all(), many=True).data)

class CreateUserSessionAPI(APIView):

    def post(self, request):
        if (request.data.get('email', None) is None):
            return Response({'error': 'email.invalid' }, status=status.HTTP_400_BAD_REQUEST)
        
        user_session = UserSession(email=request.data['email'], country=request.data['country'])

        # assign a website group to the user session
        website_groups = WebsiteGroup.objects.annotate(sessions_count=Count('user_sessions')).order_by('sessions_count', 'order')
        user_session.website_group = website_groups[0]
        user_session.save()
        return Response(UserSessionBriefSerializer(user_session).data, status=status.HTTP_201_CREATED)


class GetUserSessionAPI(APIView):
    def get(self, request, id):
      return Response(UserSessionFullSerializer(UserSession.objects.get(pk=id)).data)

class DeleteUserSessionAPI(APIView):

   def delete(self, request, id):
      return Response(UserSession.objects.get(pk=id).delete())
   

class GetUserSessionWebsitesStatusAPI(APIView):
   
   def get(self, request, user_session_id):
      user_session = UserSession.objects.get(pk=user_session_id)
      def add_status(website):
         website.completed = user_session.samples.filter(website=website).exists()
         return website
      websites = map(add_status, user_session.website_group.websites.all())
      return Response(WebsiteStatusSerializer(websites,many=True).data)