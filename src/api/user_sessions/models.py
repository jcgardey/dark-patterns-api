from django.db import models

# Create your models here.
class UserSession(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=255)
    
