# 파일을 pickle로 저장
import pickle
file_basket=open("price.pickle","wb") # "wb" : 바이너리 형태로 작성(write)
                                      # 바이너리형태로 저장하기 때면에 encoding 설정 불필요

price={"품명":"코스모스","가격":500,"색상":["화이트","핑크","레드","오렌지"]}
print(price)
pickle.dump(price,file_basket) # 위의 price에 저장된 정보를 file_basket이라는 파일에 저장
file_basket.close()

# pickle로 저장된 파일에서 정보를 불러오기
file_basket=open("price.pickle","rb") # "rb" : 바이너리 형태의 파일 읽기
price=pickle.load(file_basket) # (어떤 파일)의 정보를 불러와서 price 변수로 저장
print(price)
file_basket.close()

