# 티스토리 블로그 테스트 코드 작성

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://letminjae.tistory.com/")
time.sleep(5)

# 제일 첫번째 블로그 글 클릭
elements = driver.find_elements(By.CSS_SELECTOR, "div.post a.link")
elements[0].click()