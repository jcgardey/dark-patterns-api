from rest_framework.views import APIView
from .serializers import WebsiteGroupSerializer, WebsiteGroupWithUserSessionsSerializer
from .models import WebsiteGroup, Website
from rest_framework.response import Response
from rest_framework import status


class CreateWebsiteGroupAPI(APIView):
   
   def post(self, request):
      group = WebsiteGroup.objects.create(name=request.data['name'], order=request.data['order'])
      for website_data in request.data['websites']:
         group.websites.create(name=website_data['name'], url=website_data['url'], instructions=website_data['instructions'])
      group.save()
      return Response(WebsiteGroupSerializer(group).data, status=status.HTTP_201_CREATED)

class DeleteWebsiteGroupAPI(APIView):

   def delete(self, request, id):
      return Response(WebsiteGroup.objects.get(pk=id).delete())

class GetWebsiteGroupAPI(APIView):
   
   def get(self, request, id):
      group = WebsiteGroup.objects.get(pk=id)
      return Response(WebsiteGroupWithUserSessionsSerializer(group).data, status=status.HTTP_200_OK)

class GetAllWebsitesGroupsAPI(APIView):

   def get(self, request):
      all_groups = WebsiteGroup.objects.all()
      return Response(WebsiteGroupWithUserSessionsSerializer(all_groups, many=True).data, status=status.HTTP_200_OK)

