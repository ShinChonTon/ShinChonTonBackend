from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from irion import urls
from .views import MeetingsAPI,MeetingAPI

urlpatterns = [
    path('meetings/',MeetingsAPI.as_view()),
    path('meeting/ <int:meeting_id>',MeetingAPI.as_view()),
]
