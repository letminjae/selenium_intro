# pytest 표준에 맞춰, 셀레니움 코드 작성
import pytest
from utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestOne(BaseClass):

  def test_E2E(self):
    self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() # a[href*='shop'] : shop이 포함된 a태그

    # 블랙베리 카드 찾아 장바구니에 추가
    cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for card in cards:
      card_name = card.find_element(By.XPATH, "div/h4/a").text
      if card_name == "Blackberry":
        card.find_element(By.XPATH, "div/button").click()
        break
      
    # Checkout 클릭
    self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click() # a[class*='nav-link btn btn-primary'] : nav-link, btn, btn-primary가 포함된 a태그

    # Checkout 페이지 이동
    self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()

    # Country 입력
    self.driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(self.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    self.driver.find_element(By.LINK_TEXT, "India").click()

    # 약관 동의
    self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()

    # 구매 완료
    self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # 완료 박스 확인
    success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success!" in success_text


