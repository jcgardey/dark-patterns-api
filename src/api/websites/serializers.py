from rest_framework import serializers
from .models import WebsiteGroup, Website
from user_sessions.serializers import UserSessionFullSerializer

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('id', 'name', 'url', 'instructions', 'ux_analyzer_token')

class WebsiteGroupSerializer(serializers.ModelSerializer):
    websites = serializers.SerializerMethodField()
    
    class Meta:
        model = WebsiteGroup
        fields = ('id', 'name', 'websites', 'order')
    
    def get_websites(self, group):
        return WebsiteSerializer(group.get_websites_by_order(), many=True).data

class WebsiteStatusSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(default=False)
    class Meta:
        model = Website
        fields = ('id', 'name', 'url', 'instructions', 'completed', 'ux_analyzer_token')


class WebsiteGroupWithUserSessionsSerializer(serializers.ModelSerializer):
    user_sessions = UserSessionFullSerializer(many=True)

    class Meta:
        model = WebsiteGroup
        fields = ('id', 'name', 'user_sessions')