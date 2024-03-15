from django.db import models
from user_sessions.models import UserSession
from websites.models import Website

# Create your models here.
class Sample(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name='samples', null=True)
    website = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True)
    dark = models.BooleanField(default=False)
    questionnaire = models.JSONField()
    date = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    sample_data = models.JSONField(default=dict())