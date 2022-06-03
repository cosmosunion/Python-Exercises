# 집합(set) : 중복 허용x , 순서없음
num_basket={1,2,5,8,3,5,5,7,3}
print(num_basket) #중복 출력x

# 집합 선언하는 2가지 방법
weather1={"spring","summer","autumn"}
weather2=set(["summer","autumn","winter"])

# 교집합
print(weather1&weather2)
print(weather1.intersection(weather2))

# 합집합
print(weather1|weather2) # shift+\
print(weather1.union(weather2))

# 차집합
print(weather1-weather2)
print(weather1.difference(weather2))

# 집합에 정보 추가
weather1.add("winter")
print(weather1)

# 집합에서 정보 삭제
weather1.remove("summer")
print(weather1)

