class Service:
    secret = "영구는 배꼽이 두 개다."
    name = ""

    def __init__(self, name):
        self.name = name
        print("멤버변수 '%s' 을/를 초기화 하였습니다." % self.name)

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

    def __del__(self):
        print("저희 서비스를 이용해 주셔서 감사합니다.")

input() # 그냥 커서 깜빡이고
pey = Service("전수범") # 엔터 치면 실행

input()
pey.sum(3, 4)
input()