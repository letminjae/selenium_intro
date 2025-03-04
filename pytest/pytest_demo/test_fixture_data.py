import pytest

@pytest.mark.usefixtures("dataLoad")
class TestData:

  def test_editProfile(self,dataLoad):
      print(dataLoad)
      print("프로필 수정")
