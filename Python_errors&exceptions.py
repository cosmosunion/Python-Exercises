  # 예외 처리 (try, except)
def Divide(a,b):
  return a//b

try:
  a=int(input("첫번째 수 입력 : "))
  b=int(input("두번째 수 입력 : "))
  print("[시스템] {}를 {}로 나눈 값은 {}입니다.".format(a,b,Divide(a,b)))
except ZeroDivisionError as e: # 내장 예외 클래스 ZeroDivisionError에 속한 오류메시지를 변수 e에 담는다.
  print(e)  # 오류메시지 담은 변수 e를 print()로 출력
except ValueError: # ValueError에 해당하는 에러가 발생할 경우 아래의 코드를 실행하게 한다.
  print("ValueError 오류메시지")


  # 사용자 정의 예외 처리 (raise)
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
    raise StringError("사용자가 정의한 오류입니다.")
  print("[시스템] {}를 {}로 나눈 값은 {}입니다.".format(a, b, Divide(a, b)))
except StringError as e:
  print(e)