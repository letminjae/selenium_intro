# 웹 요소를 지정하여 자동화 테스트를 수행

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# 진짜 중요! - 요소 지정 방법
# ID, Xpath, CSS Selector, Class Name, Name, Tag Name, Link Text, Partial Link Text
# 위의 방법들을 이용하여 요소를 지정할 수 있음

#By는 selenium.webdriver.common.by에 정의되어 있음
driver.find_element(By.NAME, "email").send_keys("hello@hello.com") # By.NAME을 이용하여 요소를 지정
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456") # By.ID를 이용하여 요소를 지정
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("hello") # By.CSS_SELECTOR를 이용하여 요소를 지정
driver.find_element(By.ID, "exampleCheck1").click()
