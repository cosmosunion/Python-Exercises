# isinstance(확인대상,데이터타입) : 
# 객체가 클래스로 만들어진 인스턴스(instance)인지 확인하는 함수

# < 대상의 데이터타입 확인 >
# 숫자 1이 정수형(int형)인지 확인 → True
print(isinstance(1, int))

# 숫자 1이 실수형(float형)인지 확인 → False
print(isinstance(1, float))

# 문자 'cosmos'가 문자열(str형)인지 확인 → True
print(isinstance("cosmos",str))

# 리스트 group=[1,2,3,4]가 리스트(list)형인지 확인 → True
group=[1,2,3,4]
print(isinstance(group,list))

# < 대상이 해당 클래스로 만들어진 '인스턴스(instance'인지 확인 → True
class Unit:
  def __init__(self):
    return

test=Unit()
print(isinstance(test,Unit))
