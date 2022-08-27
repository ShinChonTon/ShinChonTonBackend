from django.db import models


class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    si = models.CharField(max_length=10, default='')
    gu = models.CharField(max_length=10, default='')
    dong = models.CharField(max_length=10, default='')
    detail_loc = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
