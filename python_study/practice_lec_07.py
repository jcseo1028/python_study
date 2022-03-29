
# 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# 전달값과 반환값

# def deposit(balance, money): # balance, money 는 전달값.
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money # 반환값.

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission # 여러값도 리턴 가능. tuple 형태의 반환값. 


# balance = 1000
# balance = deposit(balance, 10000)
# balance = withdraw(balance, 5000)
# commission, balance = withdraw_night(balance, 5000)

# 기본값

# def profile(name, age, main_lang): # \ 는 줄바꿈 문자
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "python")
# profile("김태호", 25, "Java")

# def profile(name, age = 17, main_lang = "Java"): # \ 는 줄바꿈 문자
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값

# def profile(name, age, main_lang): # \ 는 줄바꿈 문자
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}"\
#         .format(name, age, main_lang))

# profile(age=20, name="가나다", main_lang="Java") # 함수 호출 시, 순서대로 넣지 않고
# profile(main_lang="Python", age=17, name="라마바") # 키워드로 사용 가능함.

# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name : {0}\tAge : {1}\tLanguages :".format(name, age), end = " ") # end 는 줄 바꿈 문자를 공백으로 변경
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 25, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 27, "Kotlin", "Swift", "", "", "")

# def profile(name, age, *language): # *을 붙임으로서 가변적인 arguments 입력이 가능해짐.
#     print("Name : {0}\tAge : {1}\tLanguages :".format(name, age), end = " ") 
#     for lang in language:
#         print(lang , end=" ")
#     print()

# profile("유재석", 25, "Python", "Java", "C", "C++", "C#", "Git")
# profile("김태호", 27, "Kotlin", "Swift")

# 지역변수(함수내부)와 전역 변수

# gun = 10
# def checkpoint(soldiers):
#     # gun = 20 # 함수내부와 바깥쪽에 같은 이름 가능하지만 서로 다른 변수임.
#     global gun # 함수 외부의 변수를 이용하고자 할 경우. 추천되는 방법은 아님.
#     gun -= soldiers
#     print("[함수 내 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun -= soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# gun = checkpoint_ret(gun, 2)
# print("전체 총 : {0}".format(gun))

# 퀴즈

def std_weight(height, gender): # height : Cm 단위, gender : "남자" or "여자"

    weight_factor = 22
    if gender == "여자":
        weight_factor = 21

    weight = height/100 * height/100 * weight_factor
    # weight = int(weight*100)/100 # 소수점 두 자리 표시. 다른 방법이 있을 거 같은데..
    weight = round(weight, 2)

    return weight

height = 170
gender = "남자"
# gender = "여자"
weight = std_weight(height, gender)
print("키 {0}Cm {2}의 표준체중은 {1} Kg 입니다".format(height, weight, gender))