# client > 비밀번호를 잊었어요 > 새로운 비밀번호 입력 과정

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

email = "cmjj0824@naver.com"
password = "qwer1234!" #plain password

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

