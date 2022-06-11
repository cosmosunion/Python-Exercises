
# 변수 사이 띄어쓰기
print("Cosmos","Lily","Rose")

# 변수 사이 띄어쓰기 없음
print("Cosmos"+"Lily"+"Rose")

# 변수 사이에 일정값 적용 가능(how it 'sep'erates)
print("Cosmos","Lily","Rose", sep=" vs ")

# 문장 마지막 값 변경 후 다음 문장이 바로 위치 = 한 줄 표현 가능
print("Cosmos","Lily","Rose", sep="-",end=" 중에 ")
print("저는 Cosmos를 가장 좋아합니다.")

# sys.stdout / sys.stderr
import sys
print("Cosmos","Lily",file=sys.stdout) # 표준출력
print("Cosmos","Lily",file=sys.stderr) # 표준에러

# 딕셔너리 생성 후 .items()로 호출 -> 문자열(str) 정렬 변경
flowers={"Cosmos":20,"Lily":312,"Rose":1000}
for flower,price in flowers.items():
  print(flower.ljust(6),str(price).rjust(4),sep=": ")

# 대기순번표 출력 (ex: 001,002,003..)
for num in range(1,101):
  print("대기번호 : "+str(num).zfill(3))
  # .zfill(숫자) 는 숫자만큼 표시하되 앞 빈공간을 숫자 0으로 채움