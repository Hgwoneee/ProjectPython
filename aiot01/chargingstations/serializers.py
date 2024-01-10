# chargingstations/api/serializers.py
from rest_framework import serializers
from .models import ChargingStation, Charger


class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = ['chgerId','stat','chgerType']

class ChargingStationSerializer(serializers.ModelSerializer):
    charger = ChargerSerializer(many=True)
    class Meta:
        model = ChargingStation
        fields = '__all__'
