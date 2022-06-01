print("a"+"b") 
print("a", "b") #띄어쓰기 포함

# 방법1
# 정수:%d / 문자하나:%c / 문자열:%s (다 가능)
print("나는 %d살 입니다" %20)
print("나는 %s를 좋아해요" %"Cosmos")
print("Cosmos는 %c로 끝나요" %"s")
print("나는 %s와 %s을 좋아해요" %("Cosmos",3))

# 방법2
print("나는 {}살입니다".format(20))
print("나는 {}와 {}을 좋아해요".format("Cosmos",3))
print("나는 {1}와 {0}을 좋아해요".format("Cosmos",3))

# 방법3
print("나는 {favnum}와 {flower}를 좋아해요".format(flower="Cosmos", favnum=3))

# 방법4
# f"~" : 내용(~)안의 중괄호{}값은 실제 변수값을 갖고와서 사용 가능
flower="Cosmos"
favnum=3
print(f"나는 {flower}와 {favnum}를 좋아해요")

