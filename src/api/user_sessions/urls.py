from django.urls import path
from user_sessions.api import CreateUserSessionAPI, GetUserSessionsAPI
from samples.api import CreateSampleAPI

urlpatterns = [
    path('', GetUserSessionsAPI.as_view()),
    path('new', CreateUserSessionAPI.as_view()),
    path('<int:user_session_id>/samples/new', CreateSampleAPI.as_view()),
]