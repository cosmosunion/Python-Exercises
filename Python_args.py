# 가변인자를 이용한 함수 호출
# end=" "는 print()문이 끝날 때 줄바꿈을 하지 않고 다음 내용 출력

def create(name, age, *item):
  print("이름: {0}\n나이: {1}\n아이템: ".format(name,age), end="")
  for each_item in item:
    print(each_item,end=" ")
  print()
create("Cosmos",20,"sword","bread","repair-kit","tent")
create("Lily",19,"water","fish","skill-book")

