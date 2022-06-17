# Test1 클래스로 만들어진 인스턴스(객체)는 print()로 출력 불가능
# => str 이나 repr메소드를 클래스 내에 정의함으로써 print() 출력 가능
class Test1:
  def __init__(self):
    pass

# str과 repr메소드 모두 클래스 내 정의 될 경우 우선순위 : str > repr
class Test2:
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return "repr함수값입니다."
  def __str__(self):
    return "str함수값입니다."

class Test3:
  def __repr__(self):
    return "repr함수값입니다."
  def __init__(self,name):
    self.name=name    
a=Test1()    
b=Test2("테스트2")
c=Test3("테스트3")

print(a)
print(b)
print(c)


