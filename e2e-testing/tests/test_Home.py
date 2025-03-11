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
        # basics/locator.py에 있는 코드 가져오기
        homepage = Homepage(self.driver)