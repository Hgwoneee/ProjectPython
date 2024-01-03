# utils.py

import requests
from urllib import parse
from bs4 import BeautifulSoup
from .models import ChargingStation

def fetch_and_save_charging_stations(api_key):
    url = "http://apis.data.go.kr/B552584/EvCharger/getChargerInfo"

    api_key_decode = parse.unquote(api_key)

    params = {
        "ServiceKey": api_key_decode,
        "pageNo": 1,
        "numOfRows": 1000
    }

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "xml")
    items = xml.find_all("item")
    for item in items:
        ChargingStation.objects.create(
            addr=item.find("addr").text.strip(),
            statNm=item.find("statNm").text.strip(),
            statId=item.find("statId").text.strip(),
            chgerId=item.find("chgerId").text.strip(),
            chgerType=item.find("chgerType").text.strip(),
            lat=float(item.find("lat").text.strip()),
            lng=float(item.find("lng").text.strip())
        )

# Usage:
api_key_utf8 = "EpUhD8WnDkKZKfH5rj1U7C9Y5hCObQbwGjbEU00ZYw0lWevnETv7%2BlHjECr%2F0%2BJaWN9K1SW10Fzj8IsBkaGOWQ%3D%3D"
fetch_and_save_charging_stations(api_key_utf8)
