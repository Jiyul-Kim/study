import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

for i in range(1,5):
    url = "https://brand.naver.com/lge/category/314d43ffb957443a93d9c0065d7deecc?st=POPULAR&dt=IMAGE&page={}&size=40.".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":"_2JNGs4jSgu"})

    for item in items:
        # 제품 명
        name = item.find("strong", attrs={"class":"_302VwnbenP"}).get_text() # 제품명
        # 가격
        price = item.find("div", attrs={"class":"_1mmRWfKb9U"}) # 가격
        if price:
            price = price.get_text()
            price = price.strip(" 부터")
        else: 
            continue

        # 리뷰 수
        review_cnt = item.select("div._37hGc1Naih>em._2CsgrUT3NU")[0]
        if review_cnt:
            review_cnt = review_cnt.text
            review_cnt = review_cnt.replace(',','')
        else: 
            continue
                 
        # 평점
        rate_cnt = item.select("div._37hGc1Naih>em._2CsgrUT3NU")[1]
        if rate_cnt:
            rate_cnt = rate_cnt.text
        else: 

            continue    

        link = item.a["href"]

        # 평균 4.5 , 리뷰 수 100개 이상
        if float(rate_cnt) >= 4.5 and int(review_cnt) >=100:
            print(f"제품 명 : {name}")
            print(f"가격 : {price}")
            print(f"리뷰 수 : {review_cnt}")
            print(f"평점 : {rate_cnt}")
            print("바로가기 : {}".format(link))
            print("-"*100)
        else: continue
        
        # print('제품 명:',name, '가격:',price, '리뷰 수:',review_cnt, '평점:',rate_cnt)


