Cosmos="Cosmos is a flower"

print(Cosmos.lower())
print(Cosmos.upper())
print(Cosmos[0].isupper()) # 값:boolean
print(len(Cosmos)) #문자열 길이
print(Cosmos.replace("Cosmos","Rose"))

print(Cosmos.index("o"))
print(Cosmos.index("o",Cosmos.index("o")+1))
# 아니면 searching=Cosmos.index("o")로 변수를 선언/치환 가능
searching=Cosmos.index("o")
print(searching)
print(Cosmos.index("o",searching+1))

print(Cosmos.find("o"))
"""
index함수는 원하는 값이 없을 때 프로그램 종료
find함수는 -1을 표시하고 다음 코드 진행
"""

print(Cosmos.count("o")) # 갯수 세기

