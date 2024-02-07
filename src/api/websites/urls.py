from django.urls import path
from websites.api import CreateWebsiteGroupAPI

urlpatterns = [
    path('new', CreateWebsiteGroupAPI.as_view()),
]