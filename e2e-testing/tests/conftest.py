# 픽스쳐 정의 - 셀레니움 드라이버 코드 작성
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") # 크롬창 최대
    chrome_options.add_experimental_option("detach", True) # 크롬창이 바로 꺼지는 현상을 방지

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("")
    driver.maximize_window()