from django.db import models


# Create your models here.

class WebsiteGroup(models.Model):
    name = models.CharField(max_length=255)

class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    instructions = models.TextField()
    group = models.ForeignKey(WebsiteGroup, on_delete=models.CASCADE, related_name='websites')