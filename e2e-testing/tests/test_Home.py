# angular practice 의 Home 관련한 테스트
import pytest
from utilities.base_class import BaseClass
from page_objects.HomePage import Homepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

class TestHome(BaseClass):

    def test_formSubmissin(self):
        # basics/locator.py에 있는 코드 가져와서 리팩토링
        homepage = Homepage(self.driver)

        homepage.enterEmail().send_keys("hello@hello.com")
        homepage.enterPassword().send_keys("123456")

        homepage.enterName().send_keys("hello") 
        homepage.checkCheckbox().click()

        # 드롭다운 - Select를 사용한다
        dropdown = homepage.selectDropdown()
        dropdown.select_by_visible_text("Female") # Female 선택 후
        time.sleep(1)
        dropdown.select_by_index(0) # Mail 선택

        # Submit
        homepage.submitForm().click()
        message = homepage.getAlertSuccessMessage()
        print(message)