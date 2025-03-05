import pytest
from pytest_demo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestData(BaseClass):

  def test_editProfile(self,dataLoad):
      log = self.getLogger()
      log.info(dataLoad[0])
      log.info(dataLoad[2])
      # print(dataLoad)
      # print("프로필 수정")
