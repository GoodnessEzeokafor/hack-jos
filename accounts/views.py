from django.shortcuts import render

from . import serializers
from . import models
# from .forms import UserCreationForm

from rest_framework import generics
from django.views.generic.edit import CreateView

# Create your views here.




# class UserCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Participator.objects.all()
#     serializer_class =  serializers.UserSerializers




class ParticipantList(generics.ListCreateAPIView):
	queryset = models.Participant.objects.all()
	serializer_class = serializers.ParticipantSerializer


class ParticipantsDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset	 = models.Participant.objects.all()
	serializer_class = serializers.ParticipantSerializer


class TeamList(generics.ListCreateAPIView):
	queryset = models.Team.objects.all()
	serializer_class = serializers.TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Team.objects.all()
	serializer_class = serializers.TeamSerializer
	

# class Par
