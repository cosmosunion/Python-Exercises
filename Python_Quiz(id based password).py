url="http://daum.net"

pre_id=url.replace(url[0:7],"")
pre_id=pre_id[:pre_id.index(".")]

pw=pre_id[:3]+str(len(pre_id))+str(pre_id.count("e"))+"!"
print("생성된 비밀번호 : ",pw)


