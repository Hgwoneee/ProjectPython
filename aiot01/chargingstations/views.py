# views.py
from rest_framework import generics
from .models import ChargingStation
from .serializers import ChargingStationSerializer

class ChargingStationListCreateView(generics.ListCreateAPIView):
    queryset = ChargingStation.objects.all()
    serializer_class = ChargingStationSerializer

