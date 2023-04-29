import requests
import pprint # json 데이터가 줄바꿈 해서 나오지 않고 한 줄로 나올 때 유용함!
import openpyxl


client_id = "NQiH7_sc1SAtNUlef0Rp"
client_secret = "8rqvp8AYlW"

start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 20
excel_sheet.column_dimensions['D'].width = 100
excel_sheet.append(['랭킹', '제목', '가격', '링크'])


for index in range(10):
    start_num = start + (index * 100)
    naver_open_api = "https://openapi.naver.com/v1/search/shop.json?query=17인치노트북&display=100&start="+ str(start_num)
    header_params = {"X-Naver-Client-id":client_id, "X-Naver-Client-Secret":client_secret} # 일종의 JSON임
    res = requests.get(naver_open_api, headers=header_params)
    print(naver_open_api)

    if res.status_code == 200: # 응답코드 200이면 정상. open API도 응답코드가 해당됨
        data = res.json()
        # pprint.pprint(data)
        for item in data['items']:
            num += 1
            excel_sheet.append([num, item['title'], item['lprice'] ,item['link']])
    else: print("Error Code: ", res.status_code) 

excel_file.save('shopping_with_notebook_17inch.xlsx')