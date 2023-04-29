import requests
from bs4 import BeautifulSoup

url = "https://ridibooks.com/books/4327004735?_rdt_sid=category_1600&_rdt_idx=0"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url , headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# webtoons = soup.find_all("div", attrs={"class":"info_title_with_badge"})
# title = webtoons[0].span.get_text()
# viewers = soup.find_all("div", attrs={"class":"table_cell book_status direct_view_wrapper"})
# link = viewers[0].button["data-book-id"]
# print("https://view.ridibooks.com/books/"+link)

# # for 문에 인덱스 두 개 필요하면 zip() 사용하면 됨!!
# for webtoon, viewer in zip(webtoons, viewers):
#     title = webtoon.span.get_text()
#     link = "https://view.ridibooks.com/books/"+viewer.button["data-book-id"]
#     print(title,link)

# MB 평균 구하기
webtoons = soup.find_all("li", attrs={"info_size"})
for webtoon in webtoons:
    rate=webtoon.span.get_text
    print(rate)