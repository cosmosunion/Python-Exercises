# random 모듈의 shuffle/sample 함수

from random import *

users=range(1,21)
print(type(users)) 
users=list(users)
print(type(users))

# print(type(list(range(1,21)))) 으로 한번에 type 표시도 가능

users.sort() # 순서대로 정렬 (range->list로 순서없이 변경 : shuffle())
print(users)

winners=sample(users,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 {0}".format(winners[1:])) 
# 앞서 sample()로 변수 4개 가져왔기때문에 1:4로 써주지 않아도 가능
print("-- 축하합니다 --")


