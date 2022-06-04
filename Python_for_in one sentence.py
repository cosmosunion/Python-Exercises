failed=[3,8,10]

for applicant in range(1,16):
  if applicant in failed:
    continue
  else:
    print("{0}번 참가자는 입장하십시오".format(applicant))
    continue


