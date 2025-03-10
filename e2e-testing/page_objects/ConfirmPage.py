# 컨펌 페이지 관련 요소 클래스

from selenium.webdriver.common.by import By

class ConfirmPage:

  def __init__(self, driver):
    self.driver = driver

  confirmBtn = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
  submitBtn = (By.CSS_SELECTOR, "input[type='submit']")
  successText = (By.CLASS_NAME, "alert-success")

  def getConfirmButton(self):
    return self.driver.find_element(*ConfirmPage.confirmBtn)
  
  def getSubmitButton(self):
    return self.driver.find_element(*ConfirmPage.submitBtn)
  
  def getSuccessText(self):
    return self.driver.find_element(*ConfirmPage.successText).text