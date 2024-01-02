import requests
import pprint


#인증키 입력
decoding = 'EpUhD8WnDkKZKfH5rj1U7C9Y5hCObQbwGjbEU00ZYw0lWevnETv7+lHjECr/0+JaWN9K1SW10Fzj8IsBkaGOWQ=='

#url 입력
url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerStatus'
params ={'serviceKey' : decoding, 'pageNo' : '1', 'numOfRows' : '10', 'period' : '5', 'zcode' : '11' }

response = requests.get(url, params=params)
print(response.content)
# xml 내용
content = response.text

# 깔끔한 출력 위한 코드
pp = pprint.PrettyPrinter(indent=4)