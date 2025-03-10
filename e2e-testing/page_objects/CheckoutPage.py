# 체크아웃 페이지 관련 요소 클래스

from selenium.webdriver.common.by import By

class CheckoutPage:

  def __init__(self, driver):
    self.driver = driver

  cardTitle = (By.CSS_SELECTOR, ".card-title a")
  cardFooter = (By.CSS_SELECTOR, ".card-footer button")

  def getCardTitles(self):
    return self.driver.find_elements(*CheckoutPage.cardTitle)
  
  def getCardFooter(self):
    return self.driver.find_elements(*CheckoutPage.cardFooter)