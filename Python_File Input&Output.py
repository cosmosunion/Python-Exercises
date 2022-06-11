# 파일 입출력
# w : 쓰기 위한 목적(write)
# a : 이미 있는 파일에 정보를 추가(append)
# r : 읽기 위한 목적(read)

# 파일을 생성하고 정보 쓰기
file_basket=open("price.txt","w", encoding="utf8") # encoding="utf8" 한글 출력
print("코스모스 : 100", file=file_basket)
print("장미 : 300", file=file_basket)
print("백합 : 400", file=file_basket)
file_basket.close() # 파일은 마지막에 반드시 close

# 이미 존재하는 파일에 정보 추가
file_basket=open("price.txt","a",encoding="utf8")
file_basket.write("안개꽃 : 50")
file_basket.write("\n선인장 : 800") # \n 줄바꿈
file_basket.close()

# 이미 존재하는 파일의 정보를 읽어오기
file_basket=open("price.txt","r",encoding="utf8")
print(file_basket.read()) # 한번에 모든 내용 불러오기
file_basket.close()

# 파일에서 정보를 한 줄씩 따로 불러오기
file_basket=open("price.txt","r",encoding="utf8")
print(file_basket.readline(),end="") # 줄 별로 읽기/커서 아래 이동
print(file_basket.readline(),end="")
print(file_basket.readline(),end="")
print(file_basket.readline(),end="")
print(file_basket.readline(),end="")
file_basket.close()

# 파일 내 정보의 양을 모를 때 전부 출력
file_basket=open("price.txt","r",encoding="utf8")
while True: # 무한 루프 until break
  line=file_basket.readline()
  if not line: #'더이상 읽어올 정보가 없을 경우'
    break
  print(line,end="")
file_basket.close()

# 파일 내 정보를 list형태로 저장 : .readlines
file_basket=open("price.txt","r",encoding="utf8")
list_basket=file_basket.readlines()
for list in list_basket: # list 형태로 저장 후 한 줄씩 불러오기
  print(list,end="")
file_basket.close()


