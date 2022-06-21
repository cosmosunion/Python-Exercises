
  # 퀴즈에서 제시한 에러 조건을 모두 클래스로 Exception 상속을 받은 후 except 블록에서 호출하는 경우
chicken=10
waiting=1

class ValueError(Exception):
  def __init__(self,msg):
    self.msg=msg
  def __str__(self):
    return self.msg

class SoldOutError(Exception):
  def __init__(self,msg):
    self.msg=msg
  def __str__(self):
    return self.msg

while(True): # while반복문 바로 (조건없이) 실행
  try:
    print("[남은 치킨 : {}]".format(chicken))
    order=int(input("치킨을 몇 마리 주문하시겠습니까? "))
    if order>chicken:
      print("재료가 부족합니다.")
    elif order<=0:
      raise ValueError("잘못된 값을 입력하였습니다.")
    else:
      print("[대기번호: {}] {}마리 주문이 완료되었습니다.".format(waiting,order))
      waiting+=1
      chicken-=order
      if chicken==0:
        print("[남은 치킨 : {}]".format(chicken))
        raise SoldOutError("재고가 소진되어 더이상 주문을 받지 않습니다.")
  except ValueError as e:
    print(e)
  except SoldOutError as e:
    print(e)
    break


  # 퀴즈에서 제시한 에러 조건에 대한 오류메시지를 직접 출력하는 경우  
class SoldOutError(Exception):
  pass  

chicken=10
waiting=1    

while(True): 
  try:
    print("[남은 치킨 : {}]".format(chicken))
    order=int(input("치킨을 몇 마리 주문하시겠습니까? "))
    if order>chicken:
      print("재료가 부족합니다.")
    elif order<=0:
      raise ValueError
    else:
      print("[대기번호: {}] {}마리 주문이 완료되었습니다.".format(waiting,order))
      waiting+=1
      chicken-=order
    if chicken==0:
      print("[남은 치킨 : {}]".format(chicken))
      raise SoldOutError  
  except ValueError:
    print("잘못된 값을 입력하였습니다.")
  except SoldOutError:
    print("재고가 소진되어 더이상 주문을 받지 않습니다.")
    break

