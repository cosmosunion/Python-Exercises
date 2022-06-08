gender=input("성별을 입력해주세요(예:남자) : ")
height=float(input("키를 입력해주세요 : "))

def std_weight(height,gender):
  if gender=="남자":
    return height*height*22 # std_weight(height,gender)값으로 출력값 반환
  else:
   return height*height*21

weight=round(std_weight(height/100,gender),2) # round(함수값,소수점밑자리)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))

