# chargingstations/models.py

from django.db import models

class ChargingStation(models.Model):
    addr = models.CharField(max_length=255, null=True)
    statNm = models.CharField(max_length=100, null=True)
    statId = models.CharField(max_length=50, null=True)
    chgerId = models.CharField(max_length=50, null=True)
    chgerType = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        db_table = "Station"
