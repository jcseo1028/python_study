# 문자열

# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "파이썬은 쉬워요."
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

# 슬라이싱

# jumin = "781028-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # index 0 ~ 1 까지 가져오려면 2라고 해야 함. 0 부터 2 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[0:6])
# print("생년월일 : " + jumin[:6]) # index 0 부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:14]) # index 7부터 14 직전까지
# print("뒤 7자리 : " + jumin[7:]) # index 7부터 끝까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤 기준 7 번째부터 끝까지

# 문자열 처리 함수

# python = "Python is Amazing!"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) # True
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)

# index = python.index("n", index + 1) # 2 번째 "n" 의 index
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # -1, 찾는 값이 없을 경우.
# # print(python.index("Java")) # Error

# print(python.count("n")) # 2, 문자열 내 "n" 의 개수

# 문자열 포맷

# print("A" + "B")
# print("A", "B") # , 는 띄어쓰기

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")

# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("파랑", "노랑"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파랑", "노랑"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "노랑"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="노랑"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="노랑", age=20))

# v3.6 이상부터 적용됨.
# age = 20
# color = "노랑"

# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자

# print("백문이 불여일견\n백견이 불여일타") # \n 은 줄바꿈.

# print("저는 "누구누구"입니다") # Error
# print("저는 '누구누구'입니다")
# print('저는 "누구누구"입니다')
# print("저는 \"누구누구\"입니다")
# print("저는 \'누구누구\'입니다")

# print("D:\Workspace") # ? 왜 에러 안나지?
# print("D:\\Workspace")

# print("Red Apple\rPine")  # PineApple, \r 은 커서를 맨 앞으로 

# print("Redd\bApple") # RedApple, \b 는 백스페이스

# print("Red\tApple") # Red   Apple, \t 는 탭

# 퀴즈

site = "http://naver.com"
s1 = site[7:] # site.replace("http://", "") 이것도 가능
print(s1) # naver.com , http:// 제외

s2 = s1[:s1.find(".")] # s1.index(".") 도 가능.
print(s2) # naver, .com 제외

password = s2[:3] + str(len(s2)) + str(s2.count("e")) + "!" # nav51!
print("{0} 의 비밀번호는 {1} 입니다.".format(site, password))