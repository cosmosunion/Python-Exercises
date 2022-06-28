import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


alba_url = "http://www.alba.co.kr"
    
def extract_SuperBrand(url): # 알바천국 메인페이지에서 수퍼브랜드 리스트 추출
  SBlinks = []
  URLrequests = requests.get(url)
  URLsoup = BeautifulSoup(URLrequests.text, "html.parser")
  SBs = URLsoup.find("div", {"id":"MainSuperBrand"}).find("ul",{"class":"goodsBox"}) # SBs = 수퍼브랜드 링크 접근
  SBs = SBs.find_all("li")
  for SB in SBs :
    SB = SB.find("a",{"class":"goodsBox-info"})["href"]
    SBlinks.append(SB)
  return SBlinks # 링크 주소들

def extract_data(links): 
  details = []
  for link in links: # 각 링크에서 추출한 html에 대해 아래의 value 정리 
    link = requests.get(link)
    link_soup = BeautifulSoup(link.text, "html.parser")
    detail = link_soup.find("tr", {"class":""})
    place = detail.find("td",{"class":"local first"}).text.strip() # 근무지
    title = detail.find("span",{"class":"company"}).text.strip() # 회사명
    time = detail.find("td",{"class":"data"}).find("span").text.strip()  # 근무시간
    pay = detail.find("td",{"class":"pay"}).text.strip()# 급여
    date = detail.find("td",{"class":"regDate last"}).text.strip() # 작성일
    details.append({"place":place, "title":title, "time":time, "pay":pay, "date":date})
  return details

def create_file(links,details):
  for link in links:
    link_requests = requests.get(link)
    link_soup = BeautifulSoup(link_requests.text, "html.parser")
    company = link_soup.find("head").find("title").text
    company = company[:-11]
    file = open(f"{company}.csv", mode = "w")
    writer = csv.writer(file) 
    writer.writerow(["place", "title", "time", "pay", "date"])
    writer.writerow(details.value())
      

links_SuperBrand = extract_SuperBrand(alba_url) # 수퍼브랜드 링크 리스트들 추출 + csv 파일 이름+첫줄 생성
details = extract_data(links_SuperBrand)
create_file(links_SuperBrand, details)
