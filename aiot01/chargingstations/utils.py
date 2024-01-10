from datetime import datetime
from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup
from .models import ChargingStation, Charger

def fetch_and_save_charging_stations(api_key):
    url = "http://apis.data.go.kr/B552584/EvCharger/getChargerInfo"

    api_key_decode = unquote(api_key)

    params = {
        "ServiceKey": api_key_decode,
        "pageNo": 1,
        "numOfRows": 2000
    }

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "xml")
    items = xml.find_all("item")

    # 주소를 기준으로 충전소를 그룹화하여 처리
    charging_stations = {}
    for item in items:
        address = item.find("addr").text.strip()
        stat_id = item.find("statId").text.strip()

        if address not in charging_stations:
            station = ChargingStation.objects.create(
                addr=address,
                statNm=item.find("statNm").text.strip(),
                statId=stat_id,
                lat=float(item.find("lat").text.strip()),
                lng=float(item.find("lng").text.strip()),
                useTime=item.find("useTime").text.strip(),
                parkingFree=item.find("parkingFree").text.strip(),
                statUpdDt=datetime.strptime(item.find("statUpdDt").text.strip(), '%Y%m%d%H%M%S')
            )
            charging_stations[address] = station
        else:
            station = charging_stations[address]

        charger_data = {
            "chgerId": item.find("chgerId").text.strip(),
            "chgerType": item.find("chgerType").text.strip(),
            "stat": item.find("stat").text.strip()
        }

        charger = Charger.objects.create(
            chgerId=charger_data["chgerId"],
            chgerType=charger_data["chgerType"],
            stat=charger_data["stat"]
        )
        station.charger.add(charger)

        # 각 충전기 정보에 대한 상세 정보 가져오기

