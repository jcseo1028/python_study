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


# 다양한 출력 포맷

# 파일 입출력

# pickle

# with

# 퀴즈