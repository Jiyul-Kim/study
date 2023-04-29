import requests
from bs4 import BeautifulSoup

service_key = "sazAHYwWJMw1LdkwztAMMgJRBCnqGf1tPuY8DBzYyiU2CjGP7o4h/cJIVtHpZ3tAwuNtuvtHqzSdTPte/Na0WA=="
params = '&returnType=xml&numOfRows=100&pageNo=1&searchDate=2023-04-12&InformCode=PM10'

open_api = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey=" + service_key + params

res = requests.get(open_api)

soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all("item")
for item in data:
    grade = item.find('informgrade')
    cause = item.find('informcause')
    print(cause, grade)