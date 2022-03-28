
# if
# weather = "비"
# weather = "미세먼지"
# weather = "맑음"

# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input("현재 온도는? "))

# if 30 <= temp :
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp and 30 > temp :
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# for, 반목문

# for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5

# while index >=1 :
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("{0}, 커피는 폐기되었습니다.".format(customer))
# print("while 문 종료.")

# customer = "아이언맨"
# index = 1
# while True:     # 무한 반복 시
#     print("{0}, 커피가 준비되었습니다. {1} 번 호출중입니다.".format(customer, index))

#     index += 1
#     # if index > 10 :
#     #     break
# print("while 문 종료.")

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
# print("while 문 종료.")

# continue, break

# absent = [2, 5] 
# no_book = [7]
# for student in range(1, 11) :
#     if student in absent:  # absent list 안에 student 가 있는 지 검사
#         continue # 다음 반복 진행.
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0} 은 교무실로!".format(student))
#         break # 반복문 종료.
#     print("{0}, 책 읽어봐.".format(student))
# print("for 문 종료.")

# 한줄 for

# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [i.upper() for i in students]
# print(students)

# Quiz

from random import *

matched_customer = 0
for customer in range(1, 51) : # 1 ~ 50 까지
    dd_time = randrange(5, 51) # 5 ~ 50 까지
    if 5 <= dd_time <= 15:
        matched = "O"
        matched_customer += 1
    else:
        matched = " " 

    print("[{0}] {1} 번째 손님 (소요시간 : {2} 분) ".format(matched, customer, dd_time))

print("총 탑승 승객 : {0} 명".format(matched_customer))