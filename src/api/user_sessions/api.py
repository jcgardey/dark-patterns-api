from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserSession
from .serializers import UserSessionSerializer

class GetUserSessionsAPI(APIView):
    def get(self, request):
      return Response(UserSessionSerializer(UserSession.objects.all(), many=True).data)

class CreateUserSessionAPI(APIView):

    def post(self, request):
        if (request.data.get('email', None) is None):
            return Response({'error': 'email.invalid' }, status=status.HTTP_400_BAD_REQUEST)
        user_session = UserSession.objects.create(email=request.data['email'], country=request.data['country'])
        return Response(UserSessionSerializer(user_session).data, status=status.HTTP_201_CREATED)
