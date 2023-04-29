import requests
import pprint # json 데이터가 줄바꿈 해서 나오지 않고 한 줄로 나올 때 유용함!

client_id = "NQiH7_sc1SAtNUlef0Rp"
client_secret = "8rqvp8AYlW"

naver_open_api = "https://openapi.naver.com/v1/search/news.json?query=android"
header_params = {"X-Naver-Client-id":client_id, "X-Naver-Client-Secret":client_secret} # 일종의 JSON임
res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200: # 응답코드 200이면 정상. open API도 응답코드가 해당됨
    data = res.json()
    # pprint.pprint(data)
    for idx, item in enumerate(data['items']):
        print(str(idx+1) + '.', item['title'], '/ 링크: ',  item['link'])
else: print("Error Code: ", res.status_code) 