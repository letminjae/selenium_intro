# 파이썬 예외처리에 대한 기본 코드 공부

# raise Exception("Error Message") - 예외 발생시키기
# assert(조건) - 가정설정문, 조건을 걸어 예외가 발생하면 에러 출력
ItemsInCart = 0

def ExceptionItemInCart(item):
  print(item)
  if item <= 1:
    raise Exception("Item in cart should be less than 1")
  else:
    print(item)
    pass
  
# ExceptionItemInCart(ItemsInCart) # Exception : Item in cart should be less than 1 - 강제로 예외 발생 처리
# assert(ItemsInCart == 1) # AssertionError - 가정설정문, 조건을 걸어 예외가 발생하면 에러 출력

# ====================================================================================================
# try, except, finally
try:
  print("try block")
  with open("filelog.txt", "r") as reader:
    reader.read()
except: # 파이썬에서는 catch가 아닌 except로 사용
  print("Error : Some how I reached this block because there is a failure in try block")
finally:
  print("finally block")