
# 표준 입출력

# print("Python", "Java", sep=", ") # sep 기본값은 공백
# print("Python", "Java", "C#", sep=" vs ") # sep 기본값은 공백

# print("Python", "Java", sep="," , end="?") # end 기본값은 줄바꿈 문자
# print("너의 선택은?") # sep 기본값은 공백

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# scores = {"수학":70, "영어":50, "코딩":100} # dictionary , 
# for subject, score in scores.items():
#     # print(subject + " : " + str(score))
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust : 왼쪽 정렬, rjust : 오른쪽 정렬

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하시오 : ")
# print("입력값 : " + answer) # 숫자도 string type 으로 입력된다.
##########################################################################################################

# 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10차리 공간을 확보
# print("{0: > 10}".format(500))

# 양수일 땐 + 표시, 음수일 땐 - 로 표시.
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸으로 _ 로 채움
# print("{0:_<+10}".format(500))
# print("{0:,>+10}".format(500))

# 세 자리마다 , 직어주기
# print("{0:,}".format(10000000000))

# 세 자리마다 , 직어주기 +,- 부호도 붙여서
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))

# 세 자리마다 , 직어주기 +,- 부호, 자리수 확보, 빈자리는 ^ 로 채우기
# print("{0:^<+20,}".format(100000000000))

# 소수점 출력
# print("{0:f}".format(5/3))

# 소수점 출력, 자리수 지정
#  print("{0:.2f}".format(5/3))
##########################################################################################################

# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # w : write, 쓰기 모드
# print("수학 : 80", file=score_file)
# print("영어 : 90", file=score_file)
# score_file.close() # 사용후에는 항상 close 처리

# score_file = open("score.txt", "a", encoding="utf8") # a : append, 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 80") # 줄바꿈 문자 추가 필요함.
# score_file.close() # 사용후에는 항상 close 처리

# score_file = open("score.txt", "r", encoding="utf8") # r : read, 읽기 모드
# print(score_file.read())
# score_file.close() # 사용후에는 항상 close 처리

# score_file = open("score.txt", "r", encoding="utf8") # r : read, 읽기 모드
# print(score_file.readline(), end = "") # 한줄 읽은 후, 커서는 다음 줄로 이동
# print(score_file.readline(), end = "") 
# print(score_file.readline(), end = "") 
# print(score_file.readline(), end = "") 
# score_file.close() # 사용후에는 항상 close 처리

# score_file = open("score.txt", "r", encoding="utf8") # r : read, 읽기 모드
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r : read, 읽기 모드
# lines = score_file.readlines() # 각 라인을 리스트 형태로 읽어 옴.
# # print(type(lines))
# for line in lines:
#     print(line, end="")
# score_file.close()
##########################################################################################################

# pickle

# import pickle
# profile_file = open("profile.pickle", "wb") # b: Binary, w:
# profile ={"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 을 profile_file 에 pickle 형태로 저장
# profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "rb") # b: Binary, r: read
# profile = pickle.load(profile_file) # file 로부터 plckle 형태로 로딩.
# print(profile)
# profile_file.close()

##########################################################################################################

# with

# import pickle
# with open("profile.pickle", "rb") as profile_file:  # with 사용 시, open/close 를 별도로 안해줘도 된다. (c# 의 using 같음.)
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.readlines())

##########################################################################################################

# 퀴즈 
for week in range(1, 11) :
    report_name = str(week) + "주차"
    with open(report_name+".txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - \n".format(week))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")


##########################################################################################################
