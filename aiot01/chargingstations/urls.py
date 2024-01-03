# chargingstations/urls.py
from django.urls import path
from .views import ChargingStationListCreateView

urlpatterns = [
    path('charging-stations/', ChargingStationListCreateView.as_view(), name='charging-stations'),
    # Other URL patterns if any
]