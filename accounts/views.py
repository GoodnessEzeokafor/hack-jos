from django.shortcuts import render

from . import serializers
from . import models
# from .forms import UserCreationForm

from rest_framework import generics
from django.views.generic.edit import CreateView

# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = models.Participator.objects.all()
    serializer_class =  serializers.UserSerializers




class UserCreateView(generics.CreateAPIView):
	pass