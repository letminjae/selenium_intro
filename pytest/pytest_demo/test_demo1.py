# pytest 첫 사용

# 터미널 실행법
# pytest test_demo1.py : 아무 정보 표시안됨 pass/fail만 표시
# pytest -v test_demo1.py : 어떤 테스트가 실행됐는지 표시됨
# py.test : 1번과 동일
# py.test -v : 2번과 동일
# py.test -v -s : print문을 통해 출력된 내용도 확인 가능
# py.test -k first : first라는 키워드를 가진 테스트만 실행
# py.test -k first -v : first라는 키워드를 가진 테스트만 실행하고 어떤 테스트가 실행됐는지 표시됨
# py.test -m smoke : smoke라는 마크를 가진 테스트만 실행
# py.test -m get : get라는 마크를 가진 테스트만 실행
# py.test -m "not smoke" : smoke 마크를 가지지 않은 테스트만 실행
# py.test -m "smoke and get" : smoke와 get 마크를 가진 테스트만 실행
# py.test -m "smoke or get" : smoke나 get 마크를 가진 테스트만 실행

def test_firstProgram():
    print("Hello")

def test_secondProgram():
    print("Good Morning")

def test_thirdProgram():
    print("Good Night")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)