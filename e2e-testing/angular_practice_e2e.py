# angularpractice 페이지 E2E 테스트

# Shop 진입 > 블랙베리 상품을 추가 > 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2) # 암시적 대기 - 전체 페이지 로딩 시간을 기다림
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.LINK_TEXT, "Shop").click()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() # a[href*='shop'] : shop이 포함된 a태그

cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for card in cards:
  card_name = card.find_element(By.XPATH, "div/h4/a").text
  if card_name == "Blackberry":
    card.find_element(By.XPATH, "div/button").click()
    break
