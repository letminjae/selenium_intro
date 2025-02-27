# 암시적대기 명시적대기

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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(2) # 암시적 대기 - 전체 페이지 로딩 시간을 기다림

# 검색
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))

for result in results:
  result.find_element(By.XPATH, "div/button").click()

# 장바구니
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# 총합 확인
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
  sum += int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10) # 명시적 대기 - n초 동안 명시적으로 설정된 시간만큼 기다림
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) # 페이지에 expected_conditions가 나타날 때까지 기다림

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
