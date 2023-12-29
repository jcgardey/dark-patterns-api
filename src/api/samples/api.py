from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sample
from .serializers import SampleSerializer

class GetSamplesAPI(APIView):
    def get(self, request):
      return Response(SampleSerializer(Sample.objects.all(), many=True).data)

class CreateSampleAPI(APIView):
   
   def post(self, request):
      sample = Sample.objects.create(
         website=request.data['website'], 
         dark=request.data['dark'], 
         questionnaire=request.data['questionnaire'], 
         sample_data=request.data['sample_data'] )
      return Response(SampleSerializer(sample).data, status=status.HTTP_201_CREATED)
