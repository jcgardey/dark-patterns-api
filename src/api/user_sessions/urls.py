from django.urls import path
from user_sessions.api import CreateUserSessionAPI, GetUserSessionsAPI, GetUserSessionAPI, DeleteUserSessionAPI
from samples.api import CreateSampleAPI

urlpatterns = [
    path('', GetUserSessionsAPI.as_view()),
    path('<int:id>', GetUserSessionAPI.as_view()),
    path('<int:id>/delete', DeleteUserSessionAPI.as_view()),
    path('new', CreateUserSessionAPI.as_view()),
    path('<int:user_session_id>/samples/new', CreateSampleAPI.as_view()),
]