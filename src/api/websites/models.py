from django.db import models


# Create your models here.
class WebsiteGroup(models.Model):
    name = models.CharField(max_length=255)
    order = models.SmallIntegerField()

    def get_websites_by_order(self):
        return [item.website for item in self.website_items.all().order_by('order')]

class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    instructions = models.TextField()
    ux_analyzer_token = models.CharField(null=True, max_length=255)

    def is_dark(self):
        return 'enabled=true' in self.url
        
class WebsiteInGroup(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    group = models.ForeignKey(WebsiteGroup, on_delete=models.CASCADE, related_name='website_items')
    order = models.SmallIntegerField()