# 픽스쳐란 프리컨디션처럼 테스트 셋업을 해야하는 조건 설정에 대한 부분이다. == 애너테이션
import pytest

# @pytest.fixture()
# def init():
#     print("픽스쳐 셋업..")
#     yield
#     print("저는 yield 때문에 마지막에 실행돼요")

# def test_fixtureDemo(init): # 파라미터에 fixture 설정한 setup 함수를 넣어준다.
#     print("픽스쳐 실행")

@pytest.mark.usefixtures("setup") # usefixtures 사용 시 클래스 self에 픽스쳐가 자동으로 입력된다.
class TestExample:

    def test_fixtureDemo1(self):
        print("픽스쳐 실행 1")

    def test_fixtureDemo2(self):
        print("픽스쳐 실행 2")

    def test_fixtureDemo3(self):
        print("픽스쳐 실행 3")