from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
import json
from django.http import StreamingHttpResponse

from .models import Sample
from .serializers import SampleSerializer
from user_sessions.models import UserSession
from websites.models import Website

import datetime
class GetSamplesAPI(APIView):
    def get(self, request):
      return Response(SampleSerializer(Sample.objects.all(), many=True).data)

class CreateSampleAPI(APIView):
   
   def post(self, request, user_session_id, website_id):
      sample = UserSession.objects.get(pk=user_session_id).samples.create(
         website=Website.objects.get(pk=website_id), 
         dark=request.data['dark'], 
         questionnaire=request.data['questionnaire'], 
         sample_data=request.data['sample_data'],
         start= datetime.datetime.fromisoformat(request.data['start']),
         end= datetime.datetime.fromisoformat(request.data['end']),
         )
      return Response(SampleSerializer(sample).data, status=status.HTTP_201_CREATED)

class DeleteSampleAPI(APIView):

   def delete(self, request, id):
      return Response(Sample.objects.get(pk=id).delete())


class Echo:
    def write(self, value):
        return value

class ExportSamplesAPI(APIView):

   def get(self, request):

      def filter_samples(filter):
         samples = Sample.objects.all()
         if filter == 'first_round':
            return [ sample for sample in samples if sample.user_session.is_first_round_sample(sample) ]
         elif filter == 'follow_up_completed':
            return [ sample for sample in samples if sample.user_session.is_follow_up_group_completed() ]
         return samples

      def format_row(sample):
         return [
            sample.user_session.id,
            sample.user_session.email, 
            sample.website.name,
            sample.website.is_dark(), 
            sample.start, 
            sample.end, 
            sample.questionnaire['trustworthy'], 
            sample.questionnaire['frustrating'], 
            sample.questionnaire['confusing'], 
            sample.questionnaire['experience'], 
            sample.sample_data
         ]
      pseudo_buffer = Echo()
      writer = csv.writer(pseudo_buffer)
      rows = list(map(format_row, filter_samples(request.GET.get('filter', 'all'))))
      header = [["id", "usuario", "website", "dark", "start", "end", "trustworthy", "frustrating", "confusing", "experience", "sample_data"]]
      return StreamingHttpResponse (
        (writer.writerow(row) for row in (header + rows)),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="muestras.csv"'},
      )
