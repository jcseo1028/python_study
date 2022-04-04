
# 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 탱크2 새로 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# # 공격 함수
# def attack(name, location, damage):
# 	print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시" , damage) # 마린 공격 명령
# attack(tank_name, "1시" , tank_damage) # 탱크 공격 명령
# attack(tank2_name, "1시" , tank2_damage) # 탱크2 공격 명령

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) # 마린1 생성. 전달값으로 name, hp, damage 를 전달
# marine2 = Unit("마린", 40, 5) # 마린2 생성
# tank = Unit("탱크", 150, 35) # 탱크 생성

##########################################################################################################

# _init_ : 생성자

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린") # Error, __init__ 에 정의된 개수만큼 전달값 필요.
# marine2 = Unit("마린", 40)  # Error, __init__ 에 정의된 개수만큼 전달값 필요.
##########################################################################################################

# 멤버변수

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버변수 접근

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloaking = True # 빼앗은 레이스만을 위한 특별한 멤버변수 정의

# if wraith2.cloaking == True: # 클로킹 상태라면?
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 에러 발생, 정의된 멤버변수 외에 객체별로 멤벼변수를 만들 수 있으나, 다른 객체에서는 참조 불가.
# if wraith1.cloaking == True: # 우리가 만든 레이스 클로킹 여부
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))

##########################################################################################################

# 메소드

# class AttackUnit: # 공격 유닛
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     # attack 메소드 정의
#     def attack(self, location): # 전달 받은 방향으로 공격
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
    
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# 파이어뱃 : 공격 유닛, 화염방사기. 
# firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
# firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
# firebat1.damaged(25) # 남은 체력 25
# firebat1.damaged(25) # 남은 채력 0

##########################################################################################################

# 상속

# 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# 공격 유닛
# class AttackUnit(Unit): # 상속되는 Unit 을 () 에 지정
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp) # 상속된 class 의 생성자 
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기. 
# firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
# firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
# firebat1.damaged(25) # 남은 체력 25
# firebat1.damaged(25) # 남은 채력 0

##########################################################################################################

# 다중 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed

    def fly(self, name, location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable): # 여러개 class 상속 가능
    def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self, name, hp, damage) # 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed) # 공중 이동 속도

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동 속도
valkyrie.fly(valkyrie.name, "3시") # 3시 방향으로 발키리를 이동
##########################################################################################################

# 메소드 오버라이딩
##########################################################################################################

# pass
##########################################################################################################

# super
##########################################################################################################

# 스타크래프트 전반전
##########################################################################################################

# 스타크래프트 후반전
##########################################################################################################

# 퀴즈