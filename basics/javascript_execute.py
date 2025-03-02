# 셀레니움으로 웹 자바스크립트 실행하기

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# JavaScript를 실행 - excute_script
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤을 맨 아래로 내림
time.sleep(2)

# 스크린샷 날짜별로 저장
# 날짜별 폴더 생성
today = datetime.today().strftime("%Y-%m-%d")
print(today)
save_folder = os.path.join("screenshots", today)
os.makedirs(save_folder, exist_ok=True)

# 파일 저장
file_name = f"screenshot_{datetime.now().strftime('%H:%M:%S')}.png"
file_path = os.path.join(save_folder, file_name)

driver.save_screenshot(file_path)
print(f"스크린샷 저장 완료: {file_path}")
