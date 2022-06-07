# 기본값 설정

from random import *
name=input("생성하실 마법사 ID: ")
hp=randrange(100,1000)
mp=randrange(10,100)

def character(name,hp,mp,job="magician"):
  print("\n이름 : {0}\nhp : {1}\nmp : {2}\n직업 : {3}".format(name,hp,mp,job))
  
character(name,hp,mp)

