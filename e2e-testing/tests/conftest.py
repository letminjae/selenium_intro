# 픽스쳐 정의 - 셀레니움 드라이버 코드 작성
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# pytest addoption으로 여러 브라우저(크롬, 파이어폭스, 사파리..) 띄우기
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    selenium_options = Options()
    selenium_options.add_argument("--start-maximized")
    selenium_options.add_experimental_option("detach", True) # 크����이 바로 ���지는 현상을 방지
    
    # browser_name이 크롬일 때
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=selenium_options)
    # browser_name이 파이어폭스일 때
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=selenium_options)
    # browser_name이 사파리일 때
    elif browser_name == "safari":
        driver = webdriver.Safari(options=selenium_options)
    
    # 웹사이트 창 주소
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # driver 모듈 import 시 필요사항
    request.cls.driver = driver

    yield # test 실행 이후 드라이버를 닫아준다.
    driver.close()