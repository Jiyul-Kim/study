
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터 (해상도) 높이인 1080 위치로 스크린 내리기
# browser.execute_script("window.scrollTo(0,1080)") # 1920 * 1080 
# browser.execute_script("window.scrollTo(0,2080)") # 1920 * 2080 

# 화면 가장 아래로 스크롤 내릭
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval =2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs = {"class":"Epkrse"})
    # if title:
    #     print(title.get_text())
    # else: 
    #     print("찾기 실패")
    #     continue


    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "<할인되지 않은 영화 제외>")
        continue

    
    # 할인 된 가격
    price = movie.find("span", attrs = {"class":"VfPpfd VixbEe"}).get_text()

    # 링크
    link= movie.find("a", attrs = {"class":"Si6A0c ZD8Cqc"})["href"]
    # https://play.google.com + link

    
    print(f"제목 : {title.get_text()}")
    print(f"할인 전 가격 : {original_price}")    
    print(f"할인 된 가격 : {price}")
    print(f"링크 : ", "https://play.google.com"+link)
    print("-----------------------------------------")
