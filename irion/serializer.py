from rest_framework import serializers

from .models import User, Meeting, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','nickname','birth']


class MeetingSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    participant = UserSerializer(read_only=True)
    class Meta:
        model= Meeting
        fields=['id','author','location','participant','name','body','max_people','plan_date','create_date','thema','age']



# class Meeting(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meeting_author')
#     location = models.ForeignKey(Location, related_name='meeting_location')
#     participant = models.ManyToManyField(User,  related_name='meeting_participant', blank=True)
#     name = models.CharField(max_length=300)
#     max_people = models.IntegerField(null=True)
#     plan_date = models.DateTimeField( blank= True)
#     create_date = models.DateTimeField(auto_now_add= True)
#     thema = models.CharField(blank= True) # 운동, 영화, 등등
#     age = models.CharField(max_length=100) # 20대. 30대, 전연령
    
#     access_token = models.CharField(null=True, max_length=255)
#     refresh_token = models.CharField(null=True, max_length=255)
#     password = models.CharField(null=True, max_length=100)
    


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['si', 'gu', 'dong', 'detail_loc', 'latitude', 'longitude']
