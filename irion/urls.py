from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from irion import urls
from .views import LocationView

app_name = 'irion'

urlpatterns = [
    path('location/', LocationView.as_view()),
]
