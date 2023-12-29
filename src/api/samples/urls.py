from django.urls import path
from samples.api import GetSamplesAPI, CreateSampleAPI

urlpatterns = [
    path('', GetSamplesAPI.as_view()),
    path('', CreateSampleAPI.as_view()),
]