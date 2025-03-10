# 홈페이지 관련 요소 클래스

from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import CheckoutPage

class Homepage:
  def __init__(self, driver):
    self.driver = driver
  
  shop = (By.CSS_SELECTOR, "a[href*='shop']")

  # Locator 설정 - 튜플로 설정했으니, 언패킹 연산자인 *을 꼭 붙여주자!
  def shopItems(self):
    self.driver.find_element(*Homepage.shop).click()
    checkoutPage = CheckoutPage(self.driver)
    return checkoutPage
