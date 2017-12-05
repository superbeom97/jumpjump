class Service: #1
    secret = "영구는 배꼽이 두 개다."

pey = Service()
pey.secret # 얘는 멤버변수라서 바로 출력 안 됨 -> print(pey.secret) 해야 출력 되고

class Service: #2
    secret = "영구는 배꼽이 두 개다."
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s입니다." % (a, b, result))

pey = Service()
pey.sum(3,4) # 애들은 멤버함수니까 바로 print 없어도 바로 출력 됨

class Service: #3
    secret = "영구는 배꼽이 두 개다."
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service()
pey.setname("전수범") # 애들은 멤버함수니까 바로 print 없어도 바로 출력 됨
pey.sum(3,6) # 애들은 멤버함수니까 바로 print 없어도 바로 출력 됨