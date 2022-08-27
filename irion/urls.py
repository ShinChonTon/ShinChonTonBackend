from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from .views import LoginView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
=======
from irion import urls
from .views import MeetingsAPI,MeetingAPI

urlpatterns = [
    path('meetings/',MeetingsAPI.as_view()),
    path('meeting/ <int:meeting_id>',MeetingAPI.as_view()),
>>>>>>> 619a8f03b537e717f38ddf19437c44cc12f93409
]
