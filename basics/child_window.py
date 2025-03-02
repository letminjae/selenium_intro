# 기존 웹에서 자식 웹으로 진입 시 컨트롤 방법이 필요한 경우

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click() # 자식창으로 이동

# driver.switch_to.window 를 사용한다.
windows_opened = driver.window_handles # 현재 열린 창들의 리스트. 0번째는 부모창, 1번째는 자식창
driver.switch_to.window(windows_opened[1]) # 자식창으로 switch!
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() # 자식창 닫기
driver.switch_to.window(windows_opened[0]) # 부모창으로 switch!
# 부모창에서 Open a new window 확인
assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text