import requests
from bs4 import BeautifulSoup

url = "https://series.naver.com/novel/home.series"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

webfictions = soup.find_all("span", attrs={"class":"author"})
# class 속성이 "author"인 엘리먼트를 모두 반환
for webfiction in webfictions:
    print(webfiction.get_text())