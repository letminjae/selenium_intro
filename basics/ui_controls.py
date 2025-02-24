# 여러 UI 컨트롤 해보기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 1. 체크박스
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2": # Option1, Option2, Option3
        checkbox.click()
        assert checkbox.is_selected()
        break

# 2. 라디오버튼
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()

# 3. hide-show
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# 4. 자바스크립트 경고창
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Minjae")
driver.find_element(By.ID, "alertbtn").click()
# driver.switch_to : 드라이버(크롬창)에 대한 alert, iframe, window 등을 제어할 수 있음
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "Minjae" in alert_text
time.sleep(2)
alert.accept() # 확인 버튼