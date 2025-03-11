# 셋업 픽스쳐 재사용 증가를 위한 Base Class 생성

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

@pytest.mark.usefixtures('setup')
class BaseClass:

  def verifyLinkPresence(self, text):
    wait = WebDriverWait(self.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

  def selectOptionByText(self, locator):
    sel = Select(locator)
    # sel.select_by_visible_text(text)
    time.sleep(1)
    sel.select_by_index(1)