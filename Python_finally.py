  # finally
  # ①try문이 실행되든, ②예외 처리된 오류가 발생하든, ③일반적인 오류가 발생하든 무조건 실행된다.
class StringError(Exception):
  def __init__(self,msg):
    self.msg=msg
  def __str__(self):
    return self.msg

def Divide(a, b):
  return a // b

try:
  print("1부터 20까지의 수만 입력해주세요")
  a = int(input("첫번째 수 입력 : "))
  b = int(input("두번째 수 입력 : "))
  if a >20 or b>20:
    raise StringError("예외 처리된 오류입니다. ")
  print("[시스템] {}를 {}로 나눈 값은 {}입니다.".format(a, b, Divide(a, b)))
except StringError as e:
  print(e)
except:
  print("일반적인 오류입니다.")
finally:
  print("finally절은 무조건 출력됩니다.")


