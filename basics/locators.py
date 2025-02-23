# 웹 요소를 지정하여 자동화 테스트를 수행

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

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

# CSS Selector를 이용하여 요소를 지정하는 방법
# tagname[attribute='value'] 로 지정
# 또는 "find_elements"로 여러개 요소중 하나를 지정해서 사용할 수도있다.
# elements = driver.find_elements(By.CSS_SELECTOR, "input.form-control") # find_elements를 이용하여 여러개 요소를 지정
# elements[0].send_keys("hello")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("hello") # By.CSS_SELECTOR를 이용하여 요소를 지정
driver.find_element(By.ID, "exampleCheck1").click()

# 드롭다운 - Select를 사용한다
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female") # Female 선택 후
# dropdown.select_by_index(1) # Femail 선택
time.sleep(1)
dropdown.select_by_index(0) # Mail 선택

# Xpath를 이용하여 요소를 지정하는 방법
# //tagname[@attribute='value'] 로 지정
driver.find_element(By.XPATH, "//input[@type='submit']").click() # By.XPATH를 이용하여 요소를 지정
message = driver.find_element(By.CLASS_NAME, "alert-success").text # By.CLASS_NAME을 이용하여 요소를 지정 - 여러개 클래스 네임이 있을경우 아무거나 가능
print(message)
