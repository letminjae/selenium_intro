# Base Class

import logging
import inspect

class BaseClass:
  def getLogger(self):
      loggerName = inspect.stack()[1][3] # inspect.stack() : 현재 함수의 정보를 가져옴, [1][3] : 현재 함수의 이름을 가져옴
      logger = logging.getLogger(loggerName)

      # 중요! fileHandler! 로그 파일이 출력되어야하는 파일 위치정보를 가지고 있는 객체
      fileHandler = logging.FileHandler('logfile.log')
      formatter = logging.Formatter("%(asctime)s : %(name)s : %(message)s") # 시간:이름:메시지 출력
      fileHandler.setFormatter(formatter)

      logger.addHandler(fileHandler) # 로거가 어떤 파일을 출력될 것인지?

      logger.setLevel(logging.DEBUG) # 로그를 출력할 수준을 설정 

      return logger

