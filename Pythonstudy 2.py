import os
import requests

while True: 
  print("Welcome to IsItDown.py!")
  urls=input("Please write a URL or URLs you want to check. (separated by comma)\n")
  urls=urls.split(",") # urls = str(input()).lower().split(",")
  # print(urls) # 리스트형
  check_urls=[]
  for url in urls:
    url=url.strip() # strip 메소드는 리스트형에 쓸 수 없으므로 for문안에 넣어준다.
    url=url.lower() # input() 값으로 받는 순간에 lower, split 처리
    if "." not in url:
      print(f"{url} is not a valid URL")
      break
    if "http://" not in url:
      url="http://"+url
      check_urls.append(url)
    else:
      pass
    try:
      url_status=requests.get(url)
      if url_status.status_code == 200:
        print(f"{url} is up!")
      else:
        print(f"{url} is down!")
    except:
      print(f"{url} is down!")      

  try:
    while True:
      restart = input("Do you want to start over? [Y/N] ")    
      if restart not in ["y", "Y", "n", "N"]:
        print("That's not a valid answer")
        continue
      elif restart in ["y", "Y"]:
        os.system('clear')
        break
      elif restart in ["n", "N"]:
        raise
  except:
      print("k, bye!")
      break

# 코드 리뷰
# 정답과 비교했을 때 객체지향적인 사고가 필요함 
# : main(), restart() 함수 2개를 순환시키는 것으로 반복문 가능 (while true 사용하지 말자)


# 정답안
# import os
# import requests

# def restart():
#   answer = str(input("Do you want to start over? y/n ")).lower()
#   if answer == "y" or answer =="n":
#     if answer == "n":
#         print("k. bye!")
#         return
#     elif answer == "y":
#       main()
#   else:
#     print("That's not a valid answer")
#     restart()


# def main():
#   os.system('clear')
#   print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
#   urls = str(input()).lower().split(",")
#   for url in urls:
#     url = url.strip()
#     if "." not in url:
#       print(url, "is not a valid URL.")
#     else:
#       if "http" not in url:
#         url = f"http://{url}"
#       try:
#         request = requests.get(url)
#         if request.status_code == 200:
#           print(url,"is up!")
#         else:
#           print(url, "is down!")
#       except:
#           print(url, "is down!")
#   restart()


# main()