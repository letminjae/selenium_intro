# 웹페이지 내에 있는 iframe, 외부 프레임을 컨트롤하는 방법
# iframe은 웹페이지 내에 다른 웹페이지를 포함하는 태그로, 웹페이지 내에 다른 웹페이지를 포함하는 방법을 제공한다.
# 즉, 자식창과 비슷하게 switch를 해야하는 절차를 지나야한다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # 크롬창 최대
chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/iframe")

# Alert 삭제
driver.find_element(By.CSS_SELECTOR, ".tox-notification__dismiss.tox-button.tox-button--naked.tox-button--icon").click()

# iframe 으로 switch - frame 입력 후, frame ID 파라미터에 입력
driver.switch_to.frame("mce_0_ifr")

# 사용자가 iframe text를 막아놔서 수정이 안되는 경우, contenteditable 속성을 true로 변경
driver.execute_script("arguments[0].setAttribute('contenteditable', 'true');", driver.find_element(By.ID, "tinymce"))

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hello World")

# 다시 원래 페이지로 돌아가기
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text) # An iFrame containing the TinyMCE WYSIWYG Editor
