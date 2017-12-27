# 구글 입사문제 중에서

# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

c = ['1238888188008']
c_arrage = str(c)
#print(c)
#print(c_arrage)
#print(c.count('8'))
#print(c_arrage.count('8'))

d= ['1','2','3','8888','18','80','0','8']
list = str(d)
#print(list.count('8'))


# 내 시도 // 변수로 list 쓰지 말자..
number = range(1, 10001)  # 1부터 10,000까지 정의한 건 좋았어.
list = str(number) # 근데 range로 잡은 걸 리스트(list)로 바꿔야 하는데, 문자열(str)로 바꾸는 것만 생각했어
print(list.count('8')) # 리스트(list)로 먼저 바꾸고 문자열(str)로 바꿔야 했다..!

# 올바른 방식
number = range(1, 10001)
a = list(number)
b = str(a)
print(b.count('8'))

# 위 코드를 한 줄에 다 모아서 적은,,
print(str(list(range(1, 10001))).count('8'))