# chargingstations/models.py
from django.db import models

class ChargingStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    # 추가 필드들을 정의할 수 있음

    class Meta:
        # Table이름을 "User"로 정한다. default 이름은 user_user가 된다.
        db_table = "Station"