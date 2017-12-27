# 문자열 01
pin="881120-1068245"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)

# 문자열 02
pin="881120-1068234"
print(pin[7])

# 리스트01
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# ★리스트02
a=['Life', 'is', 'too', 'short']
result=" ".join(a)
print(result)

# ★튜플
a=(1,2,3)
a=a+(4,)
print(a)

# 딕셔너리
a={'a':90,'b':80,'c':70}
result=a.pop('b')
print(a)
print(result)

# 집합
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
print(list(aSet))
# 또는
aSet=set(a)
b=list(aSet)
print(list(b))