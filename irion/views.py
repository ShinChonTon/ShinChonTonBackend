from http.client import HTTPResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializer import LocationSerializer

from .models import Location
from .serializer import LocationSerializer


class LocationView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


def location(request):
    if request.method == "GET":
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

# @csrf_exempt
# def location(request, pk):
#     try:
#         locations = Location.objects.get(pk=pk)
#     except Location.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == "GET":
#         # locations = Location.objects.all()
#         serializer = LocationSerializer(locations, many=True)
#         return JsonResponse(serializer.data)
