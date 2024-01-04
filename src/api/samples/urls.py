from django.urls import path
from samples.api import GetSamplesAPI, DeleteSampleAPI

urlpatterns = [
    path('', GetSamplesAPI.as_view()),
    path('<int:id>/delete', DeleteSampleAPI.as_view()),
]