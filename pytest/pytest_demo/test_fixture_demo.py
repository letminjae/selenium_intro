# 픽스쳐란 프리컨디션처럼 테스트 셋업을 해야하는 조건 설정에 대한 부분이다. == 애너테이션
import pytest

@pytest.fixture()
def setup():
    print("픽스쳐 셋업..")
    yield
    print("저는 yield 때문에 마지막에 실행돼요")

def test_fixtureDemo(setup): # 파라미터에 fixture 설정한 setup 함수를 넣어준다.
    print("픽스쳐 실행")