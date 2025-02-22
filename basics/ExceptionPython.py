ItemsInCart = 0

def ExceptionItemInCart(item):
  print(item)
  if item <= 1:
    raise Exception("Item in cart should be less than 1")
  else:
    print(item)
    pass
  
ExceptionItemInCart(ItemsInCart) # Exception : Item in cart should be less than 1 - 강제로 예외 발생 처리
assert(ItemsInCart == 1) # AssertionError - 가정설정문, 조건을 걸어 예외가 발생하면 에러 출력