from django.db import models

# Create your models here.
class Sample(models.Model):
    website = models.CharField(max_length=255)
    dark = models.BooleanField(default=False)
    questionnaire = models.JSONField()
    date = models.DateTimeField(auto_now=True)
    sample_data = models.JSONField(default={})