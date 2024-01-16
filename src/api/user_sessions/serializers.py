from rest_framework import serializers
from .models import UserSession
from samples.serializers import SampleSerializer

class UserSessionBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ('email', 'country')

class UserSessionFullSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True)
    class Meta:
        model = UserSession
        fields = ('email', 'country', 'samples')