# 객체가 하나일 때 유용
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2) # 달라진 곳

print(a.first)
print(a.second)


# 또 다른 방법 _ 객체가 여러 개일 때 유용
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
FourCal.setdata(a, 4, 2) # 달라진 곳

print(a.first)
print(a.second)


# 테스트_
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
FourCal.setdata(a, 4, 2)

print(a.first)
print(a.second)

a.first = 1   # 함수를 통해 바꿀 수도 있으나, 이렇게 직접 바로 바꿀 수도 있다.
a.second = 2  # 함수를 통해 바꾸려면 4라인이 필요하나, 직접 바꾸면 2라인으로,, 간단하긴 좀 더 간단한
              # 하지만 단점은 누구나 다 고칠 수 있기 때문에, 보안에 취약하다.
              # private하게 관리하긴 어렵다. 바로 고칠 수 있으니(_파이썬에서 // 자바 c는 안 되는 듯)

print(a.first)
print(a.second)