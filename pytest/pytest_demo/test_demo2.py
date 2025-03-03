# 두번째 테스트 파일
# 그룹화 : 그룹화는 @ 키워드를 사용한다.
import pytest

@pytest.mark.smoke
@pytest.mark.skip # 수정 중인 TC가 있으니 제외 시키는 방법 - test_demo2_1만 제외!
def test_demo2_1():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_CreditCard_2():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"