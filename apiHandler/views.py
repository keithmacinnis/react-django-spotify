from apiHandler.serializers import RoomSerializer
from apiHandler.models import PartyRoom
from django.shortcuts import render
from rest_framework import generics
from .models import PartyRoom

class RoomView(generics.ListAPIView):
    queryset = PartyRoom.objects.all()
    serializer_class = RoomSerializer

