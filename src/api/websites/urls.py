from django.urls import path
from websites.api import CreateWebsiteGroupAPI, DeleteWebsiteGroupAPI, GetWebsiteGroupAPI, GetAllWebsitesGroupsAPI, GetAllWebsitesAPI, CreateWebsiteAPI, UpdateWebsiteAPI

urlpatterns = [
    path('', GetAllWebsitesAPI.as_view()),
    path('new', CreateWebsiteAPI.as_view()),
    path('<int:id>', UpdateWebsiteAPI.as_view()),
    
    path('groups', GetAllWebsitesGroupsAPI.as_view()),
    path('groups/new', CreateWebsiteGroupAPI.as_view()),
    path('groups/<int:id>/delete', DeleteWebsiteGroupAPI.as_view()),
    path('groups/<int:id>', GetWebsiteGroupAPI.as_view()),
]