from rest_framework.views import APIView
from .serializers import WebsiteGroupSerializer, WebsiteGroupWithUserSessionsSerializer, WebsiteSerializer
from .models import WebsiteGroup, Website
from rest_framework.response import Response
from rest_framework import status


class CreateWebsiteGroupAPI(APIView):
   
   def post(self, request):
      group = WebsiteGroup.objects.create(name=request.data['name'], order=request.data['order'])
      for website_id in request.data['websites']:
         group.websites.add( Website.objects.get(pk=website_id))
      group.save()
      return Response(WebsiteGroupSerializer(group).data, status=status.HTTP_201_CREATED)

class DeleteWebsiteGroupAPI(APIView):

   def delete(self, request, id):
      return Response(WebsiteGroup.objects.get(pk=id).delete())

class GetWebsiteGroupAPI(APIView):
   
   def get(self, request, id):
      group = WebsiteGroup.objects.get(pk=id)
      return Response(WebsiteGroupSerializer(group).data, status=status.HTTP_200_OK)
   
   def put(self, request, id):
      group = WebsiteGroup.objects.get(pk=id)
      websites = []
      for website_id in request.data['websites']:
         websites.append(Website.objects.get(pk=website_id))
      group.websites.set(websites)
      group.name = request.data['name']
      group.order = request.data['order']
      group.save()
      return Response(WebsiteGroupSerializer(group).data, status=status.HTTP_200_OK)

class GetAllWebsitesGroupsAPI(APIView):

   def get(self, request):
      all_groups = WebsiteGroup.objects.all()
      return Response(WebsiteGroupWithUserSessionsSerializer(all_groups, many=True).data, status=status.HTTP_200_OK)


class CreateWebsiteAPI(APIView):
   def post(self, request):
      website = Website.objects.create(
         name=request.data['name'], 
         url=request.data['url'], 
         instructions=request.data['instructions'],
         ux_analyzer_token=request.data['ux_analyzer_token'])
      return Response(WebsiteSerializer(website).data, status=status.HTTP_201_CREATED)

class UpdateWebsiteAPI(APIView):

   def put(self, request, id):
      website = Website.objects.get(pk=id)
      website.name = request.data['name']
      website.url = request.data['url']
      website.ux_analyzer_token = request.data['ux_analyzer_token']
      website.save()
      return Response(WebsiteSerializer(website).data, status=status.HTTP_200_OK)
   
class GetAllWebsitesAPI(APIView):

   def get(self, request):
      all_websites = Website.objects.all()
      return Response(WebsiteSerializer(all_websites, many=True).data, status=status.HTTP_200_OK)
      
