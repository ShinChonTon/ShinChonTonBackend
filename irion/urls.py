from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import LoginView, SignUpView

app_name = 'irion'

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]
