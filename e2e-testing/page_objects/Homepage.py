from selenium.webdriver.common.by import By

class Homepage():
  def __init__(self, driver):
    self.driver = driver
  
  shop = (By.CSS_SELECTOR, "a[href*='shop']")

  # Locator 설정 - 언패킹 연산자인 *을 꼭 붙여주자!
  def shopItems(self):
    return self.driver.find_elements(*Homepage.shop)