from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

time.sleep(1)

# 배너 한 달간 안보기 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div/div[2]/button[1]").click()
# 가는 날 선택 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click() 
time.sleep(1)


# 네이버 캘린더 xpath 규칙
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[Month(2~)]/table/tbody/tr[Week(1~)]/td[Day(1~)]/button/b

day27 = browser.find_elements(By.XPATH, '//b[text() = "27" ]')
day27[0].click()

day30 = browser.find_elements(By.XPATH, '//b[text() = "30" ]')
day30[0].click()


# 도착 버튼
arrival = browser.find_element(By.XPATH, '//b[text() = "도착" ]')   
arrival.click()

time.sleep(1)

# 국내
domestic = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]')
domestic.click()

# 제주도
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

# 항공권 검색
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))

print(elem.text)

browser.quit()
