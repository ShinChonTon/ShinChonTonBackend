from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from irion import urls


urlpatterns = [
    path('admin/', admin.site.urls),

]
