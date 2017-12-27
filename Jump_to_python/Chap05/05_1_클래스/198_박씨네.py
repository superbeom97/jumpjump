class HousePark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다" % (self.fullname, where))

pey = HousePark()
pey.setname("응용")
pey.travel("부산")

# 선생님이 원하는 방식,, 미리 변수를 설정해 주는
class HousePark:
    lastname = "박"
    fullname = ""
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다" % (self.fullname, where))

pey = HousePark()
#pey.setname("응용")
pey.travel("부산")

# p.203 __init__ 사용
class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다" % (self.fullname, where))

pey = HousePark("응용")
pey.travel("태국")