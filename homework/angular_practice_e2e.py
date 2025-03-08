# angularpractice 페이지 E2E 테스트

# Shop 진입 > 블랙베리 상품을 추가 > Checkout으로 이동 > 국가 입력 > 약관 동의 > 구매 완료

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2) # 암시적 대기 - 전체 페이지 로딩 시간을 기다림
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.LINK_TEXT, "Shop").click()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() # a[href*='shop'] : shop이 포함된 a태그

# 블랙베리 카드 찾아 장바구니에 추가
cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for card in cards:
  card_name = card.find_element(By.XPATH, "div/h4/a").text
  if card_name == "Blackberry":
    card.find_element(By.XPATH, "div/button").click()
    break

# Checkout 클릭
driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click() # a[class*='nav-link btn btn-primary'] : nav-link, btn, btn-primary가 포함된 a태그
# driver.find_element(By.XPATH, "//div[@id='navbarResponsive']/ul/li/a").click()

# Checkout 페이지 이동
driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()

# Country 입력
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

# 약관 동의
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()

# 구매 완료
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# 완료 박스 확인
success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_text)
assert "Success!" in success_text


