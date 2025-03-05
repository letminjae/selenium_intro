# pytest에서 로그를 찍는 방법
# logging 패키지를 사용

# logger 호출 > fileHandler 지정 > Formatter 커스터마이징 > addHandler 호출 > 로그레벨 설정

import logging

def test_logging_demo():
    logger = logging.getLogger(__name__) #어떤 테스트에서 로그가 찍혔는지 확인하려면 이름이 있어야한다. -> __name__

    # 중요! fileHandler! 로그 파일이 출력되어야하는 파일 위치정보를 가지고 있는 객체
    fileHandler = logging.FileHandler('logfile.log')
    logging.Formatter("%(asctime)s : %(name)s : %(message)s") # 시간:이름:메시지 출력

    logger.addHandler(fileHandler) # 로거가 어떤 파일을 출력될 것인지?

    logger.setLevel(logging.INFO) # 로그를 출력할 수준을 설정 (인포 밑 레벨까지 출력 - 지금 코드에선 디버그로그 빼고 다 출력)

    logger.debug("디버그 구문 실행됨")
    logger.info("정보 구문 실행됨")
    logger.warning("패스는 아니지만, warning으로 처리됨")
    logger.error("메이저 에러가 발견됨")
    logger.critical("크리티컬 에러가 발견됨")