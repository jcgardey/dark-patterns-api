from rest_framework import serializers
from .models import UserSession
from samples.serializers import SampleSerializer
from rest_framework import serializers

class UserSessionBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ('id', 'email', 'country')

class UserSessionFullSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True)
    class Meta:
        model = UserSession
        fields = ('id', 'email', 'country', 'samples')


