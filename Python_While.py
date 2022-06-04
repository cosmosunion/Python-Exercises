answer="Cosmos"
person=input("성함은? ")
question=input("가장 좋아하는 꽃은? ")


while question!=answer:
  print("정답이 아닙니다.")
  question=input("가장 좋아하는 꽃은? ")
if question==answer:
  print("{0}님 축하합니다. 정답입니다.".format(person))

