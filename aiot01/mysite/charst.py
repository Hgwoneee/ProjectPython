import pandas as pd
import requests
from urllib import parse
from bs4 import BeautifulSoup


url = "http://apis.data.go.kr/B552584/EvCharger/getChargerInfo"
api_key_utf8 = "EpUhD8WnDkKZKfH5rj1U7C9Y5hCObQbwGjbEU00ZYw0lWevnETv7%2BlHjECr%2F0%2BJaWN9K1SW10Fzj8IsBkaGOWQ%3D%3D"
api_key_decode = parse.unquote(api_key_utf8)

parms = {
    "ServiceKey": api_key_decode,
    "pageNo":1,
    "numOfRows":1000
}

response = requests.get(url,params=parms)
xml = BeautifulSoup(response.text,"xml")
items = xml.find("items")
item_list = []
for item in items:
    item_dict = {
        'addr':item.find("addr").text.strip(),
        'statNm':item.find("statNm").text.strip(),
        'statId':item.find("statId").text.strip(),
        'chgerId':item.find("chgerId").text.strip(),
        'chgerType':item.find("chgerType").text.strip(),
        'lat':item.find("lat").text.strip(),
        'lng':item.find("lng").text.strip()
    }
    item_list.append(item_dict)

    df = pd.DataFrame(item_list)
    print(df.iloc[-1])