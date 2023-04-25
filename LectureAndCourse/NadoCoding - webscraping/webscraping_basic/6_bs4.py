import requests
from bs4 import BeautifulSoup

url = "https://series.naver.com/novel/home.series"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 엘리먼트 출력
# print(soup.a.attrs) # a 엘리먼트의 속성 정보 출력
# print(soup.a["href"]) # a 엘리먼트의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"no1 on NPI=a:home"})) # class = "no1 on NPI=a:home" 인 a 엘리먼트를 찾아줘
# print(soup.find(attrs={"class":"no1 on NPI=a:home"})) # class = "no1 on NPI=a:home" 인 어떤 엘리먼트를 찾아줘

# print(soup.find("ul", attrs={"class" :  "bstop10_list"}))
# list1 = soup.find("li")
# print(rank01.a.get_text())
# list2 = list1.next_sibling.next_sibling
# list3 = list2.next_sibling.next_sibling

# print(list3.a.get_text())
# list2 = list3.previous_sibling.previous_sibling
# print(list2.a.get_text())

# print(list1.parent)

# list2 = list1.find_next_sibling("li")
# print(list2.a.get_text())
# list3 = list2.find_next_sibling("li")
# print(list3.a.get_text())

# print(list1.find_next_siblings)

webfiction = soup.find("a", text= "오늘만 사는 기사 [독점]")
print(webfiction)


