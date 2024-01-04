from django.urls import path
from user_sessions.api import CreateUserSessionAPI, GetUserSessionsAPI

urlpatterns = [
    path('', GetUserSessionsAPI.as_view()),
    path('new', CreateUserSessionAPI.as_view()),
    #path('<int:id>/delete', DeleteSampleAPI.as_view()),
]