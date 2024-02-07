from rest_framework import serializers
from .models import WebsiteGroup, Website

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'url', 'instructions')


class WebsiteGroupSerializer(serializers.ModelSerializer):
    websites = WebsiteSerializer(many=True)
    
    class Meta:
        model = WebsiteGroup
        fields = ('name', 'websites')