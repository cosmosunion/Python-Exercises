# 리스트:대괄호[] / 딕셔너리:중괄호{}
basket={"red":"Rose","white":"Lily",3:"Cosmos"}
print(basket)

# 딕셔너리 내 원하는 값이 없을 때 : [key] 또는 .get
# print(basket[5]) -> 출력시 프로그램 종료
print(basket.get(5)) # -> None 출력
print(basket.get(5,"Tulip")) # -> None 대신 ""값 출력

# 딕셔너리에 특정 key의 value값 존재하는지 확인 가능(as boolean)
print(3 in basket)
print(5 in basket)

# 딕셔너리에 key:value 추가
basket["yellow"]="Hibiscus"
print(basket)

# 딕셔너리에 key:value 중 중복되는 key가 있을경우 업데이트
basket[3]="Cactus"
print(basket)

# 딕셔너리에 key:value 중 중복되는 value가 있어도 정상 추가
basket["purple"]="Rose"
print(basket)

# 딕셔너리에서 key:value 삭제
del basket[3]
print(basket)

# 딕셔너리에서 key만 출력
print(basket.keys())

# 딕셔너리에서 value만 출력
print(basket.values())

# 딕셔너리에서 key, value 같이 출력
print(basket.items())

# 딕셔너리의 모든 값 삭제
basket.clear()
print(basket)



