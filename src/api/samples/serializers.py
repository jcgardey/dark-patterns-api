from rest_framework import serializers
from .models import Sample
from websites.models import Website

class WebsiteInSampleSerializer(serializers.ModelSerializer):
    is_dark = serializers.SerializerMethodField()

    def get_is_dark(self, website):
        return website.is_dark()

    class Meta:
        model = Website
        fields = ('id', 'name', 'url', 'is_dark')

class SampleSerializer(serializers.ModelSerializer):

    website = WebsiteInSampleSerializer()

    class Meta:
        model = Sample
        fields = '__all__'