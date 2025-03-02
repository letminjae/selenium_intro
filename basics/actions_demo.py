# 마우스 액션 사용

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 마우스 오버 - ActionChains 모듈 사용
action = ActionChains(driver)
# 액션 메서드 호출 후, 항상 perform() 메서드를 호출해야 한다.
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() # move_to_element() 메서드는 마우스를 해당 요소로 이동시키는 메서드
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform() # context_click() 메서드는 마우스 오른쪽 버튼을 클릭하는 메서드
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

