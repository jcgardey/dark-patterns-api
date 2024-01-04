from django.db import models
from user_sessions.models import UserSession

# Create your models here.
class Sample(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name='samples', null=True)
    website = models.CharField(max_length=255)
    dark = models.BooleanField(default=False)
    questionnaire = models.JSONField()
    date = models.DateTimeField(auto_now=True)
    sample_data = models.JSONField(default=dict())