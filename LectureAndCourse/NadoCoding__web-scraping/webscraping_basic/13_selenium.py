import time
from selenium import webdriver

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디와 패스워드 입력
browser.find_element_by_id("id").send_keys("kjekje04")
browser.find_element_by_id("pw").send_keys("wjdms4120")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(0)

# 5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("kjekje0412")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("kjekje0412")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 닫힘
browser.quit()