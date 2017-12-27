# 02-3 리스트 자료형

# 리스트에서 연속된 범위의 값 수정하기
a=[1,2,3]
print(a)
a[2]=4
print(a)
a[1]=['a','b','c']
print(a)

a=[1,2,4]
print(a)
a[1:2]=['a','b','c']
print(a)

# del 함수 사용해 리스트 요소 삭제하기
a=[1,'c',4]
del a[1]
print(a)

# 리스트 정렬 : a.sort() // 리스트 뒤집기 : a.reverse()

# 리스트에 요소 삽입_ insert(a,b) : 리스트의 a번째 위치에 b를 삽입
a=[1,2,3]
a.insert(0,4)  # a[0] 위치에 4 삽입
print(a)

a.insert(3,564)
print(a)

# 리스트 요소 제거(remove)_ remove(x) : 리스트에서 첫 번째로 나오는 x를 삭제
a=[1,2,3,1,2,3]
a.remove(3)
print(a)
a.remove(3)
print(a)
