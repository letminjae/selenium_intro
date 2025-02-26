# 암시적대기 명시적대기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# 검색
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
