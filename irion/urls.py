from xml.etree.ElementInclude import include
from django.urls import path
from irion import urls
from .views import MeetingsAPI,MeetingAPI
from .views import LocationView

app_name = 'irion'

urlpatterns = [
    path('meetings/',MeetingsAPI.as_view()),
    path('meeting/ <int:meeting_id>',MeetingAPI.as_view()),
    path('location/', LocationView.as_view()),
]
