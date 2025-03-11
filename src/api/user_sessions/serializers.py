from rest_framework import serializers
from .models import UserSession
from samples.serializers import SampleSerializer
from rest_framework import serializers
from websites.models import WebsiteGroup


class CreateUserSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSession
        fields = ('age', 'gender', 'purchases', 'country', 'email')

class UserSessionBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ('id', 'email', 'country')

class UserSessionFullSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True)
    class Meta:
        model = UserSession
        fields = ('id', 'date', 'email', 'age', 'gender', 'purchases', 'country', 'samples')
 

class WebsiteGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebsiteGroup
        fields = ('id', 'name')
class UserSessionWithWebsitesGroup(serializers.ModelSerializer):
    website_group = WebsiteGroupSerializer()
    follow_up_group = WebsiteGroupSerializer()

    class Meta:
        model = UserSession
        fields = ('id', 'date', 'email', 'website_group', 'follow_up_group')