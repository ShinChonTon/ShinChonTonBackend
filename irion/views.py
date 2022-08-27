from asyncio.windows_events import NULL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from .serializer import MeetingSerializer, UserSerializer, LocationSerializer
from .models import Meeting, User, Location

# Create your views here.

from .serializer import LocationSerializer

from .models import Location
from .serializer import LocationSerializer


class LocationView(APIView):
    def get(self, request):
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

class  MeetingsAPI(APIView):  # 미팅 전체
    
    def get(self,request):          # 미팅 정보가져오기
        meetings= Meeting.objects.all()
        serializer = MeetingSerializer(meetings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request): # request에 카테고리도 포함하여 포스트    # 넘겨줘야하는 값(user_id, name, image, category)
        author=get_object_or_404(User,id=request.data.user_id)
        location = Location.objects.get(location1=request.data.location1,location2=request.data.location2,location3=request.data.location3,location4=request.data.location4)
        serializer = MeetingSerializer(data= request.data,author=author,participant=author, location= location)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class  MeetingAPI(APIView): 
    
    def put(self, request, meeting_id):# 글 수정
        meeting=get_object_or_404(Meeting,id=meeting_id)
        serializer = MeetingSerializer(meeting, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, meeting_id):# 글 삭제
        meeting=get_object_or_404(Meeting,id=meeting_id)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
    
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meeting_author')
    # location = models.ForeignKey(Location, related_name='meeting_location')
    # participant = models.ManyToManyField(User,  related_name='meeting_participant', blank=True)
    # name = models.CharField(max_length=300)
    # max_people = models.IntegerField(null=True)
    # plan_date = models.DateTimeField( blank= True)
    # create_date = models.DateTimeField(auto_now_add= True)
    # thema = models.CharField(blank= True) # 운동, 영화, 등등
    # age = models.CharField(max_length=100) # 20대. 30대, 전연령
    
        
