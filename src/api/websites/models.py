from django.db import models


# Create your models here.

class WebsiteGroup(models.Model):
    name = models.CharField(max_length=255)
    order = models.SmallIntegerField()

class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    instructions = models.TextField()
    group = models.ManyToManyField(WebsiteGroup, related_name='websites')
    ux_analyzer_token = models.CharField(null=True, max_length=255)