from django.urls import path
from samples.api import GetSamplesAPI, CreateSampleAPI, DeleteSampleAPI

urlpatterns = [
    path('', GetSamplesAPI.as_view()),
    path('new', CreateSampleAPI.as_view()),
    path('<int:id>/delete', DeleteSampleAPI.as_view()),
]