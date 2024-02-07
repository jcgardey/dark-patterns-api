from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserSession
from .serializers import UserSessionBriefSerializer, UserSessionFullSerializer

class GetUserSessionsAPI(APIView):
    def get(self, request):
      return Response(UserSessionBriefSerializer(UserSession.objects.all(), many=True).data)

class CreateUserSessionAPI(APIView):

    def post(self, request):
        if (request.data.get('email', None) is None):
            return Response({'error': 'email.invalid' }, status=status.HTTP_400_BAD_REQUEST)
        user_session = UserSession.objects.create(email=request.data['email'], country=request.data['country'])
        return Response(UserSessionBriefSerializer(user_session).data, status=status.HTTP_201_CREATED)


class GetUserSessionAPI(APIView):
    def get(self, request, id):
      return Response(UserSessionFullSerializer(UserSession.objects.get(pk=id)).data)

class DeleteUserSessionAPI(APIView):

   def delete(self, request, id):
      return Response(UserSession.objects.get(pk=id).delete())