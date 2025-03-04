# conftest!! 테스트 파일들이 공통적으로 사용하는 fixture를 정의하는 파일
# 테스트 케이스가 여러개면? setup을 하나하나 넣어주지 말고 클래스로 정의해서 사용하자.
import pytest

@pytest.fixture()
def setup():
    print("픽스쳐 셋업..")
    yield
    print("저는 yield 때문에 마지막에 실행돼요")

@pytest.fixture()
def dataLoad():
    print("데이터 로드 중...")
    return ["김씨", "박씨", "이씨"]