# 셋업 픽스쳐 재사용 증가를 위한 Base Class 생성

import pytest

@pytest.mark.usefixtures('setup')
class BaseClass:
  pass