from rest_framework import serializers
from .models import WebsiteGroup, Website
from user_sessions.serializers import UserSessionFullSerializer

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'url', 'instructions')


class WebsiteGroupSerializer(serializers.ModelSerializer):
    websites = WebsiteSerializer(many=True)
    
    class Meta:
        model = WebsiteGroup
        fields = ('name', 'websites')

class WebsiteStatusSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(default=False)
    class Meta:
        model = Website
        fields = ('id', 'name', 'url', 'instructions', 'completed')


class WebsiteGroupWithUserSessionsSerializer(serializers.ModelSerializer):
    user_sessions = UserSessionFullSerializer(many=True)

    class Meta:
        model = WebsiteGroup
        fields = ('name', 'user_sessions')