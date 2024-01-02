import pandas as pd
import requests
from bs4 import BeautifulSoup

#  자신의 인증키를 복사해서 입력합니다.
API_KEY = 'vb6xo6YvKfYtW025%2Bs8r0l9Nb2ebfHh1lo8spyg0O7dAyMX0UMUwHEn3ufItBk2RI57o5vpvBZF1v%2BT7a7PVHQ%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)
#  print(API_KEY_decode)


req_url = "http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList"

pageNo = 1
numOfRows = 200


req_parameter = {"ServiceKey": API_KEY_decode, "pageNo": pageNo, "numOfRows": numOfRows}

r = requests.get(req_url, params=req_parameter)

xml = BeautifulSoup(r.text, "xml")
items= xml.find("items")
item_list = []
for item in items:
    item_dict = {
        'addr':item.find("addr").text.strip(),
        'chargeTp': item.find("chargeTp").text.strip(),
        'cpStat': item.find("cpStat").text.strip(),
        'cpId': item.find("cpId").text.strip(),
        'cpNm': item.find("cpNm").text.strip(),
        'csId': item.find("csId").text.strip(),
    }
    item_list.append(item_dict)

    df = pd.DataFrame(item_list)
    print(df.iloc[-1])