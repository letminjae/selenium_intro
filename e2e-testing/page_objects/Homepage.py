# 홈페이지 관련 요소 클래스

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_objects.CheckoutPage import CheckoutPage

class Homepage:
  def __init__(self, driver):
    self.driver = driver
  
  shop = (By.CSS_SELECTOR, "a[href*='shop']")
  email = (By.NAME, "email")
  password = (By.ID, "exampleInputPassword1")
  name = (By.CSS_SELECTOR, "input[name='name']")
  checkbox = (By.ID, "exampleCheck1")
  dropdown = (By.ID, "exampleFormControlSelect1")
  submit = (By.XPATH, "//input[@type='submit']")
  alertSuccess = (By.CLASS_NAME, "alert-success")

  # Locator 설정 - 튜플로 설정했으니, 언패킹 연산자인 *을 꼭 붙여주자!
  def shopItems(self):
    self.driver.find_element(*Homepage.shop).click()
    checkoutPage = CheckoutPage(self.driver)
    return checkoutPage
  
  def enterEmail(self):
    return self.driver.find_element(*Homepage.email)
  
  def enterPassword(self):
    return self.driver.find_element(*Homepage.password)
  
  def enterName(self):
    return self.driver.find_element(*Homepage.name)
  
  def checkCheckbox(self):
    return self.driver.find_element(*Homepage.checkbox)
  
  def selectDropdown(self):
    return Select(self.driver.find_element(*Homepage.dropdown))

  def submitForm(self):
    return self.driver.find_element(*Homepage.submit)
  
  def getAlertSuccessMessage(self):
    return self.driver.find_element(*Homepage.alertSuccess).text
