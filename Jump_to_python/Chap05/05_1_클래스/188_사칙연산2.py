class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second # 그냥 first + second 하면 스튜삣!
        return result
    # 또 다른 방법으론 바로 'return self.fist + self.second' 라고 적어도 되긴 돼, 똑같은 내용이야
    # 디버깅할 때 윗 방법은 바로 결과를 확인할 수 있어,
    # 하지만 변수를 설정하지 않고 바로 self.fist + self.second 설정하면 디버깅할 때 복잡해
    # 윗 방법으로 (변수를 설정해서) 사용하는 게 좋다!

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

print(a.sum()) # 그냥 print(sum()) 하면 안 돼! -> 5, 6, 7 라인의 결과를 불러 온 것!