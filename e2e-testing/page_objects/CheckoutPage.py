# 체크아웃 페이지 관련 요소 클래스

from selenium.webdriver.common.by import By

class CheckoutPage:

  def __init__(self, driver):
    self.driver = driver

  cardTitle = (By.CSS_SELECTOR, ".card-title a")
  cardFooter = (By.CSS_SELECTOR, ".card-footer button")
  checkoutBtn = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
  checkoutBtnSuccess = (By.CSS_SELECTOR, "button[class*='btn btn-success']")

  def getCardTitles(self):
    return self.driver.find_elements(*CheckoutPage.cardTitle)
  
  def getCardFooter(self):
    return self.driver.find_elements(*CheckoutPage.cardFooter)
  
  def getCheckoutButton(self):
    return self.driver.find_element(*CheckoutPage.checkoutBtn)
  
  def getCheckoutButtonSuccess(self):
    return self.driver.find_element(*CheckoutPage.checkoutBtnSuccess)