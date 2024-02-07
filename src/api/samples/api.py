from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sample
from .serializers import SampleSerializer
from user_sessions.models import UserSession
from websites.models import Website

class GetSamplesAPI(APIView):
    def get(self, request):
      return Response(SampleSerializer(Sample.objects.all(), many=True).data)

class CreateSampleAPI(APIView):
   
   def post(self, request, user_session_id, website_id):
      sample = UserSession.objects.get(pk=user_session_id).samples.create(
         website=Website.objects.get(pk=website_id), 
         dark=request.data['dark'], 
         questionnaire=request.data['questionnaire'], 
         sample_data=request.data['sample_data'] )
      return Response(SampleSerializer(sample).data, status=status.HTTP_201_CREATED)

class DeleteSampleAPI(APIView):

   def delete(self, request, id):
      return Response(Sample.objects.get(pk=id).delete())
