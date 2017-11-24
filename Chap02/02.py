# 02-2 문자열 자료형

# 문자열 더해서 연결하기(Concatenation)
head="Python"
tail=" is fun!"
head+tail
print(head+tail)
'Python is fun!'

# 슬라이싱으로 문자열 나누기
a="20171124Cloudy"
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year)
2017
print(day)
1124
print(weather)
'Cloudy'

# 문자열 수정
a="Pithon"
print(a[:1])
print(a[2:])
print(a[:1]+'y'+a[2:])
print(a)
a=a[:1]+'y'+a[2:]
print(a)

# ☆문자열 삽입
# ['Life', 'is', 'too', 'short']라는 리스트를 Life is too short라는 문자열로 만들어 출력해 보자.
a=['Life', 'is', 'too', 'short']
result=" ".join(a)
print(result)

# 문자열 나누기
a="Life is too short"
a.split()
print(a.split())

a="Life is too short"
print(a.split())

a="a-b-c-d"
a.split("-")
print(a.split("-"))
