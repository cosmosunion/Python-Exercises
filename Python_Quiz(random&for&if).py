# 30명의 승객과 매칭/소요시간 5~15분 사이의 승객만

from random import *
cnt=0
for i in range(1,21):
  time=randrange(5,51)
  if 5<=time<=15:
    print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
    cnt+=1
    continue
  else:
    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0}분".format(cnt))
