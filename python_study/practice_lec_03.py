# 연산자
# print(1 + 1)
# print(3 - 2) # 1
# print(5 * 2) # 10
# print(6 / 3) # 2

# print(2 ** 3) # 2^3
# print(5 % 3) # 2
# print(10 % 3) # 1

# print(5 // 3) # 1 몫 구하기
# print(10 // 3) # 3 몫 구하기

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3 == 3) # True
# print(4 == 2) # False
# print(3+4 == 7) # True

# print(1 != 3) # True
# print(not (1 != 3 ) ) # False

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print((5 > 4 > 3)) # True
# print((5 > 4 > 7)) # False

#간단한수식

# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4
# print(number)

# number = number + 2 # 16
# print(number)

# number += 2 # 18
# print(number)

# number *= 2 # 36
# print(number)

# number /= 2 # 18
# print(number)

# number -= 2 # 16
# print(number)

# number %= 5 # 1
# print(number)

#숫자처리함수

# print(abs(-5)) # 5
# print(pow(4, 2)) # 4^2 = 16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3
# print(round(4.56)) # 4

# from math import *  # math library 에 있는 것을 모두 사용한다는 의미
# print(floor(4.54)) # 내림 연산, 3
# print(ceil(3.14)) # 올림 연산, 4
# print(sqrt(16)) # 제곱근, 4


#랜덤함수
# from random import *

# print(random()) # 0.0 이상 1.0 미만의 임의의 값을 생성.
# print(random() *10) # 0.0 이상 10.0 미만의 임의의 값을 생성.
# print(int(random() * 10)) # 0.0 이상 10.0 미만의 임의의 값을 생성. (정수)

# print(int(random() * 10) + 1) # 1 이상 10.0 이하의 임의의 값을 생성. (정수)

# print(int(random() * 45) + 1) # 1 ~ 45
# print(int(random() * 45) + 1) # 1 ~ 45
# print(int(random() * 45) + 1) # 1 ~ 45
# print(int(random() * 45) + 1) # 1 ~ 45
# print(int(random() * 45) + 1) # 1 ~ 45
# print(int(random() * 45) + 1) # 1 ~ 45

# print(randrange(1, 46)) # 1 이상 46 미만의 임의의 값을 생성 (정수)

# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)
# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)
# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)
# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)
# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)
# print(randint(1, 45)) # 1 부터 45 까지의 임의의 값을 생성. (정수)

# Quiz

from random import *
offline_day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(offline_day) + " 일로 선정되었습니다.")