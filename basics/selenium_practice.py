# 240625

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 옵션값 설정
chrome_options = Options()
# 크롬창 최대
chrome_options.add_argument("--start-maximized")
# 크롬창이 바로 꺼지는 현상을 방지
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.naver.com"

driver.get(url)
# n초를 기다리거나, 로드되면 바로 페이지 표시
driver.implicitly_wait(3)

# 검색창에 검색어 입력
query = driver.find_element(By.ID, "query")
query.send_keys("인공지능")

# 클래스나 셀렉터등 여러 요소에 지정 가능
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
search_btn.click()

# 물리적인 시간 지연
time.sleep(2)

# 페이지 종료
driver.quit()