from rest_framework import serializers
from .models import PartyRoom

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyRoom
        fields = ("id","uid","host","guest_can_pause","votes_to_skip")
