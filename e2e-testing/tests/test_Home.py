# angular practice 의 Home 관련한 테스트
from utilities.base_class import BaseClass
from page_objects.HomePage import Homepage

class TestHome(BaseClass):

    def test_formSubmissin(self):
        # basics/locator.py에 있는 코드 가져와서 리팩토링
        homepage = Homepage(self.driver)

        homepage.enterEmail().send_keys("hello@hello.com")
        homepage.enterPassword().send_keys("123456")

        homepage.enterName().send_keys("hello") 
        homepage.checkCheckbox().click()

        # 드롭다운 - BaseClass에 저장
        self.selectOptionByText(homepage.getGender())

        # Submit
        homepage.submitForm().click()
        message = homepage.getAlertSuccessMessage()
        print(message)