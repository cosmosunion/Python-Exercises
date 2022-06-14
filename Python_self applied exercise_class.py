# 클래스(Class)를 이용한 응시자 등록 및 조회 기능
recruit=[]

class candidate():
  def __init__(self):
    self.name=input("이름 : ")
    self.age=input("나이 : ")
    self.language=input("프로그래밍 언어 : ")
    recruit.append([self.name,self.age,self.language]) # append는 리스트형태의 정보에만 사용가능
  def profile(self):
    print("\n등록한 응시자 수 : {0}".format(i+1))
    
for i in range(0,5):
  new=candidate()
  new.profile()

while True:
  order=int(input("\n조회할 응시자 번호 : ")) 
  
  def inquire(order):
    print("\n<{}번째 지원자>".format(order))   
    order-=1
    print("이름 : {}\n나이 : {}\n프로그래밍 언어 : {}".format(*recruit[order]))
  
  inquire(order)
