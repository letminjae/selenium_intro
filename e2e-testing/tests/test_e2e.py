# pytest 표준에 맞춰, 셀레니움 코드 작성
import pytest
from utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.HomePage import Homepage
from page_objects.CheckoutPage import CheckoutPage

class TestOne(BaseClass):

  def test_E2E(self):
    homepage = Homepage(self.driver)
    checkoutPage = CheckoutPage(self.driver)

    homepage.shopItems().click()

    # 블랙베리 카드 찾아 장바구니에 추가
    cards = checkoutPage.getCardTitles()
    i = -1
    for card in cards:
      i = i + 1
      card_name = card.text
      if card_name == "Blackberry":
        checkoutPage.getCardFooter()[i].click()
        break
      
    # Checkout 클릭
    checkoutPage.getCheckoutButton().click()

    # Checkout 페이지 이동
    checkoutPage.getCheckoutButtonSuccess().click()

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


