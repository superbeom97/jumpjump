class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다" % (self.fullname, where))

pey = HousePark("응용")
pey.travel("태국")


# 클래스 상속
class HouseKim(HousePark): # 클래스 이름 뒤, 괄호 안에 super/parent class 명을 써주면 돼
    lastname = "김" # 공통된 것은 제외하고 공통되지 않은 다른 속성만 추가로 넣어주면 돼

juliet = HouseKim("줄리엣")
juliet.travel("독도")


# 메서드 오버라이딩 - 상속받을 대상인 클래스의 메서드와 이름은 같지만 그 행동을 다르게 해야 할 때
class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %s일 가네." % (self.fullname, where, day))

juliet = HouseKim("줄리엣")
juliet.travel("독도", 3)