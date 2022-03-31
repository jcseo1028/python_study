# 표준 입출력

# print("Python", "Java", sep=", ") # sep 기본값은 공백
# print("Python", "Java", "C#", sep=" vs ") # sep 기본값은 공백

# print("Python", "Java", sep="," , end="?") # end 기본값은 줄바꿈 문자
# print("너의 선택은?") # sep 기본값은 공백

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

scores = {"수학":70, "영어":50, "코딩":100} # dictionary , 
for subject, score in scores.items():
    print(subject + " : " + str(score))
    print(subject.ljust(8), )



# 다양한 출력 포맷

# 파일 입출력

# pickle

# with

# 퀴즈