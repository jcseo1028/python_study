
# 리스트

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호")) # 리스트 내 Item 의 Index 찾기

# subway.append("하하") # 리스트 끝에 Item 추가
# print(subway)

# subway.insert(1, "정형돈") # 리스트 내 특정 index 에 Item 추가
# print(subway)

# subway.pop()  # 리스트 끝에 Item 제거
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) # 리스트 내 특정 Item 의 개수 확인

# num_list = [5, 2, 4, 3, 1]
# num_list.sort() # sorting
# print(num_list)

# num_list.reverse() # 리스트 내 순서 뒤집기
# print(num_list)

# num_list.clear() # 리스트 내 모든 Item 삭제
# print(num_list)

# mix_list = ["조세호", 20, False]
# num_list = [5, 2, 4, 3, 1]
# print(mix_list)

# mix_list.extend(num_list) # 리스트 합치기
# print(mix_list)

# 사전 Dictionary {}

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet[3])
#print(cabinet[5]) # Error 발생.
# print(cabinet.get(5)) # None
# print(cabinet.get(5, "사용가능")) # None 대신 표시할 글자를 표시하고 싶을 경우.

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A001":"유재석", "B100":"김태호"} # String 형태의 Key 도 가능
# print(cabinet["A001"])
# print(cabinet["B100"])

# cabinet["A001"] = "김종국"  # 값 변경
# cabinet["C020"] = "조세호"  # 추가

# print(cabinet) 

# del cabinet["B100"] # Dictionary Item 삭제
# print(cabinet)

# print(cabinet.keys()) # Dictionary Key 만 출력.
# print(cabinet.values()) # Dictionary Value 만 출력.
# print(cabinet.items()) # Key, Value 쌍으로 출력.

# cabinet.clear() # Dictionary 내 모든 데이터 삭제
# print(cabinet)

# 튜플, 수정 불가능한 리스트, 접근 속도가 빠름. (,)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") # Tuple 은 수정 불가

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 집합 (Set), 중복이 안되고 순서가 없는 자료 구조

# my_set = {1, 2, 3, 3, 3}
# print(my_set) # 3 은 한번만 출력됨.

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java & python) # 두 집합의 교집합
# print(java.intersection(python)) # 두 집합의 교집합

# print(java | python) # 두 집합의 합집합
# print(java.union(python)) # 두 집합의 합집합

# print(java - python) # 두 집합의 차집합
# print(java.difference(python)) # 두 집합의 차집합

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)

# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # type(variable) : 변수의 자료형 조회
# time = 11
# print(type(time))

# menu = list(menu) # set 형 자료형을 list 로 변경
# print(menu, type(menu))

# menu = tuple(menu) # tuple 로 변환
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# {'우유', '커피', '주스'} <class 'set'>
# ['우유', '커피', '주스'] <class 'list'>
# ('우유', '커피', '주스') <class 'tuple'>
# {'우유', '커피', '주스'} <class 'set'>

# 퀴즈

from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)

# shuffle(lst) # lst 를 무작위로 섞음.
# print(lst)

# print(sample(lst, 1)) # lst 에서 무작위로 1개 선택
# print(lst)

list_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # range(1:21) 로 해도 됨. -> list 로 변경 필요
print(list_id)

# 순서를 섞음.
shuffle(list_id)
# list_id = set(list_id)
print(list_id)

# 1등 당첨자
first = sample(list_id, 1)
print(first)

# 1등 당첨자 제외
list_id.remove(first[0]) # first 도 리스트였음.
print(list_id)

# 2등 당첨자
shuffle(list_id)
print(list_id)
second = sample(list_id, 3)
print(second)

# # 당첨자 출력
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : " + str(first))
print("커피 당첨자 : " + str(second))
print("-- 축하합니다 --")