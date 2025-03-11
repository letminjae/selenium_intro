# pytest 표준에 맞춰, 셀레니움 코드 작성
import pytest
from utilities.base_class import BaseClass
from page_objects.HomePage import Homepage

class TestOne(BaseClass):

  def test_E2E(self):
    homepage = Homepage(self.driver)

    # shopItems 에서 checkout page 리턴됨
    checkoutPage = homepage.shopItems()

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

    # getCheckoutButtonSuccess()에서 Confirm Page 리턴됨
    confirmPage = checkoutPage.getCheckoutButtonSuccess()

    # Country 입력
    confirmPage.findCountries()
    self.verifyLinkPresence("India")
    confirmPage.getIndiaOption().click()

    # 약관 동의
    confirmPage.getConfirmButton().click()

    # 구매 완료
    confirmPage.getSubmitButton().click()

    # 완료 박스 확인
    success_text = confirmPage.getSuccessText()
    assert "Success!" in success_text


