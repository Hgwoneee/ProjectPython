# chargingstations/utils.py
import requests
from .models import ChargingStation

def fetch_and_save_charging_stations():
    url = 'https://example.com/api/charging_stations'  # 전기차주유소 데이터를 제공하는 API 엔드포인트
    response = requests.get(url)

    if response.status_code == 200:
        charging_stations = response.json()  # JSON 형식의 데이터로 가져옴
        for station_data in charging_stations:
            ChargingStation.objects.create(
                name=station_data['name'],
                location=station_data['location'],
                # 필요한 다른 필드들을 추가할 수 있음
            )
