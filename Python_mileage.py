# 함수생성시 전달값이 없는 경우
def join():
  print("가입을 축하드립니다.")

# 함수생성시 값을 전달하고 반환값을 받는 경우
def mileage(balance, money):
  print("포인트가 적립되어 잔액은 {0}원 입니다.".format(balance+money))
  return balance+money

balance=0
money=int(input("적립금 등록 : "))

while money>0 :
  balance=mileage(balance, money)
  money=int(input("적립금 등록 : "))

