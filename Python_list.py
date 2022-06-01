BTS=["V","정국","RM","Suga"]

# 순서 위치
print(BTS.index("RM"))

# 순서 마지막에 추가
BTS.append("진")
print(BTS)

# 순서 중간에 추가
BTS.insert(2,"지민")
print(BTS)

# 순서 마지막에서부터 하나씩 제거
BTS.pop()
BTS.pop()
BTS.pop()
print(BTS)

# 중복 아이템의 수 세기
BTS.append("V") # append : 한개만 추가
BTS.extend(["지민","지민","지민"]) # extend : 여러개 추가
print(BTS.count("V"))
print(BTS.count("지민"))

# 자동 정렬
num_list=[1,5,7,3,4,8]
num_list.sort()
print(num_list)

# 자동 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

