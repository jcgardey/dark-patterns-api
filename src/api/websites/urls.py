from django.urls import path
from websites.api import CreateWebsiteGroupAPI, DeleteWebsiteGroupAPI, GetWebsiteGroupAPI, GetAllWebsitesGroupsAPI

urlpatterns = [
    path('', GetAllWebsitesGroupsAPI.as_view()),
    path('new', CreateWebsiteGroupAPI.as_view()),
    path('<int:id>/delete', DeleteWebsiteGroupAPI.as_view()),
    path('<int:id>', GetWebsiteGroupAPI.as_view()),
]