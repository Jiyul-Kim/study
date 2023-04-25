import requests
import re
from bs4 import BeautifulSoup

url = "https://brand.naver.com/lge/category/314d43ffb957443a93d9c0065d7deecc?st=POPULAR&dt=IMAGE&page=1&size=40"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs={"class":"_2JNGs4jSgu"})
# print(items.find("span", attrs={"class":"tx_num"}).get_text())
for item in items:
    # 제품 명
    name = item.find("strong", attrs={"class":"_302VwnbenP"}).get_text() # 제품명
    # 가격
    price = item.find("div", attrs={"class":"_1mmRWfKb9U"}) # 가격
    if price:
        price = price.get_text()
        price = price.strip(" 부터")
    else: print("에러")
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회

    # 리뷰 수
    review_cnt = item.select("div._37hGc1Naih>em._2CsgrUT3NU")[0].text
    review_cnt = review_cnt.replace(',','')
    # 평점
    rate_cnt = item.select("div._37hGc1Naih>em._2CsgrUT3NU")[1].text

    # 평균 4.5 , 리뷰 수 100개 이상
    if float(rate_cnt) >= 4.5 and int(review_cnt) >=100:
        print('제품 명:',name, '가격:',price, '리뷰 수:',review_cnt, '평점:',rate_cnt)
    else: continue

    # # 평균 수

