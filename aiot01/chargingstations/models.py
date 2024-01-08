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
    useTime = models.CharField(max_length=50, null=True)
    parkingFree = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    statUpdDt = models.DateTimeField(auto_now=True, null=True)  # 변경 시간대 정보 자동 갱신


    class Meta:
        db_table = "Station"
