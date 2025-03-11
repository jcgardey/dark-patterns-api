from django.db import models
from websites.models import WebsiteGroup 

# Create your models here.
class UserSession(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    PURCHASE_CHOICES = [
        ('none', 'None'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('>6', '> 6'),
    ]

    date= models.DateTimeField(auto_now_add=True, null=True)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='other', max_length=6)
    purchases = models.CharField(choices=PURCHASE_CHOICES, default='none', max_length=6)
    website_group = models.ForeignKey(WebsiteGroup, on_delete=models.CASCADE, related_name='user_sessions', null=True)
    follow_up_group = models.ForeignKey(WebsiteGroup, on_delete=models.CASCADE, related_name='follow_ups', null=True)
    
