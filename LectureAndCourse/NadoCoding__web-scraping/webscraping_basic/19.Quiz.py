from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

url = "https://realty.daum.net/home/apt/map"
browser.get(url)

# 아파트 검색
search = browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/input')
search.click()
search.send_keys("용인동백두산위브더제니스")
time.sleep(1)
browser.find_element_by_class_name("btn-search").click()

# 매몰 클릭
time.sleep(1)
browser.find_element_by_xpath('//*[@id="sale-count-button"]/div/div/div[2]').click()


###################### 상세 정보 스크래핑 ###################### 
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# 매매 / 전세, 가격
items = soup.find_all("div", attrs={"class" : "items_text_wrap__XAudD"})
for item in items:
    price = item.find("div", attrs={"class" : "css-1563yu1 r-jwli3a r-1wbh5a2 r-1w6e6rj r-159m18f r-ubezar r-b88u0q r-135wba7"}).get_text()
    space = item.find("div", attrs={"class" : "css-1563yu1 css-vcwn7f r-jwli3a r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-16dba41 r-14yzgew r-fdjqy7 r-13wfysu r-3s2u2q r-1ad0z5i"}).get_text()
    dong_ho = item.find("div", attrs={"class" : "css-1563yu1 css-vcwn7f r-jwli3a r-1wbh5a2 r-1w6e6rj r-159m18f r-n6v787 r-16dba41 r-14yzgew r-fdjqy7 r-13wfysu r-3s2u2q r-1ad0z5i"}).get_text()    

    print(price, space, dong_ho)
# 면적
# 동
# 층
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accecpt-Language" : "ko-KR,ko"   
    }
res = requests.get(url, headers=headers)
res.raise_for_status()

browser