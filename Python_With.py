# with 
 # price 파일내 바이너리 형태로 pickel저장된 정보를 file_basket 변수에 저장
# import pickle
# with open("price.pickle","rb") as file_basket:
#   print(pickle.load(file_basket)) 

with open("review.txt","w",encoding="utf8") as file_review:
  file_review.write("코스모스가 아름답게 피었습니다.")

with open("review.txt","r",encoding="utf8") as file_review:
  print(file_review.read())

