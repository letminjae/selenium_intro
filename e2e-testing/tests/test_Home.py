# angular practice 의 Home 관련한 테스트
import pytest
from utilities.base_class import BaseClass
from page_objects.HomePage import Homepage
from test_data.HomePageData import HomePageData

class TestHome(BaseClass):

    def test_formSubmissin(self, getData):
        # basics/locator.py에 있는 코드 가져와서 리팩토링
        homepage = Homepage(self.driver)

        homepage.enterEmail().send_keys(getData["email"])
        homepage.enterPassword().send_keys(getData["password"])

        homepage.enterName().send_keys(getData["name"])
        homepage.checkCheckbox().click()

        # 드롭다운 - BaseClass에 저장
        self.selectOptionByText(homepage.getGender())

        # Submit
        homepage.submitForm().click()
        message = homepage.getAlertSuccessMessage()
        print(message)

        # 여러 데이터를 테스트할 때, 새로고침 필요
        self.driver.refresh()

    # 각각의 튜플이 하나의 테스트케이스가 된다.
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param
