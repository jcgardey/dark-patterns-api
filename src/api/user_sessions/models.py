from django.db import models
from websites.models import WebsiteGroup 

# Create your models here.
class UserSession(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=255)
    website_group = models.ForeignKey(WebsiteGroup, on_delete=models.CASCADE, related_name='user_sessions', null=True)
    
