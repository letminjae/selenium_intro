from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 크롬 실행 - webdriver.Chrome() - 기본값
# 원래 service 인자가 필요하나, chromewebdriver 설치를 해주어 필요없게 만듬 - brew install chromewebdriver
driver = webdriver.Chrome()

driver.maximize_window() # 창 최대화
driver.get("http://www.rahulshettyacademy.com")
print(driver.title) # HTML title
print(driver.current_url) # 현재 URL
driver.get("http://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.back() # 뒤로가기
driver.refresh() # 새로고침
driver.forward() # 앞으로가기
driver.close()