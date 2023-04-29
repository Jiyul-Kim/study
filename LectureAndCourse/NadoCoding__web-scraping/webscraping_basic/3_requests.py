import requests
# res = requests.get("https://www.naver.com/")
# res = requests.get("http://nanocoding.tistory.com")
res = requests.get("https://www.google.com/")
res.raise_for_status() # 올바르게 가져오면 출력, 에러가 있으면 뜸

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else: print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", 'w', encoding="utf8") as f:
    f.write(res.text)