# 생성한 모듈을 불러오는 방법 

import travel.Japan, travel.China 
# import 사용시 마지막에 올 객체이름은 항상 모듈 또는 패키지만 가능 / 함수나 클래스는 import 직접적으로 사용 불가능
# 단 from ~ import 구문에서는 패키지/모듈/함수/클래스 모두 직접적으로 import 가능
# 예: from travel.Japan import JapanPackage 

# from trave import * # travel패키지 안에 __init__모듈에 __all__ 설정을 하지 않으면 프로그램 정상 작동x
# 설정해도 발생하는 오류(물결) 표시 제거 : 설정 > Linting > Whether to lint Python files(VSCode)

while True: # 예약이 확정될때까지 무한 루프
  go_to=input("\n여행하실 국가를 입력하세요 : ")

  while go_to not in ["일본","중국"]:
    print("\n준비된 여행 상품이 없습니다.")
    go_to=input("여행하실 국가를 입력하세요 : ")
    
  if go_to == "일본":
    go_to_Japan=travel.Japan.JapanPackage("일본") 
    # go_to_Japan 이름의 객체는 앞으로 travel패키지에서 Japan 모듈에 존재하는 JapanPackage 클래스를 불러와서 실행시키는 함수를 의미
    go_to_Japan.reserve()
    # go_to_Japan.reserve() 는 travel패키지에서 Japan모듈에 존재하는 JapanPackage 클래스 내 정의된 reserve() 함수를 호출
  
  elif go_to == "중국":
    go_to_China=travel.China.ChinaPackage("중국")
    go_to_China.reserve()
    
  confirm=input("\n예약을 확정하시겠습니까? [1]예 / [2]아니오 : ")
  
  if confirm in ["예", "1"]:
    print("예약이 확정되었습니다.")
    print("이용해주셔서 감사합니다.")
    break
  elif confirm in ["아니오", "2"]:
    print("\n예약을 취소합니다.") 
    # → 코드전체를 while True로 안으로 넣음으로서 break로 강제종료하지 않는 이상 다시 코드 전체가 반복

