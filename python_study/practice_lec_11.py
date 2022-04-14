
# 모듈

# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv # theater_module 을 새로운 별명인 mv 로 사용
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # theater_module 내에서 모든 것을 가져다가 사용
# price(3) # theater_module. 필요 없음
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 모듈에서 일부만 가져다가 사용
# price(5) # 이번에는 5명
# price_morning(6)
# price_soldier(7) # import 하지 않았으므로 사용 불가

# from theater_module import price_soldier as price # price_soldier 를 새로운 별명인 price 로 사용
# price(5) # price_soldier() 를 호출

##########################################################################################################

# 패키지

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.thailand.ThailandPackage # 클래스 직접 import 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
# trip_to = ThailandPackage() # travel.thailand. 는 생략
# trip_to.detail()

# from travel import vietnam # travel 패키지에서 vietnam 모듈 가져오기
# trip_to = vietnam.VietnamPackage() # travel. 은 생략
# trip_to.detail()

##########################################################################################################

# __all__

# from travel import *
# trip_to = vietnam.VietnamPackage() # 베트남
# trip_to.detail()

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage() # 태국
# trip_to.detail()

##########################################################################################################

# 모듈 직접 실행

# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

##########################################################################################################

# 패키지, 모듈 위치

# import inspect
# import random
# print(inspect.getfile(random)) # random 모듈의 위치

# import inspect
# from travel import *
# print(inspect.getfile(thailand)) # thailand 모듈의 위치

# 작성된 패키지를 python Library 폴더로 이동하기
# https://nadocoding.tistory.com/81?category=902275

##########################################################################################################

# pip install

# https://nadocoding.tistory.com/82?category=902275

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

##########################################################################################################

# 내장함수
# https://nadocoding.tistory.com/83?category=902275

# language = input("무슨 언어를 좋아하세요? ")
# print("{0} 은/는 아주 좋은 언어입니다!".format(language))

# print(dir())
# import random # random 모듈 가져다 쓰기
# print(dir())
# import pickle # pickle 모듈 가져다 쓰기
# print(dir())

##########################################################################################################

# 외장함수
# https://nadocoding.tistory.com/84?category=902275

# import glob
# print(glob.glob("*.stats")) # 확장자가 stats 인 모든 파일

# import os
# print(os.getcwd()) # 현재 디렉토리

# import os

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# import os
# print(os.listdir())

# import time
# print(time.localtime())

# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초

# import datetime
# print("오늘 날짜는", datetime.date.today())

##########################################################################################################

# 퀴즈

import byme
byme.sign()

##########################################################################################################