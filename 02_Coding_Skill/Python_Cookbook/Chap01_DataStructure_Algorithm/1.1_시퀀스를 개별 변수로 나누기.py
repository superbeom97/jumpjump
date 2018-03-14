#### Chapter1 - 1.1 시퀀스를 개별 변수로 나누기
### [문제] N개의 요소를 가진 튜플이나 시퀀스가 있다. 이를 변수 N개로 나누어야 한다.
### [해결] 모든 시퀀스(혹은 이터레이팅 가능한 것)는 간단한 할당문을 사용해서 개별 변수로 나눌 수 있다.
###        단 한 가지 주의해야 할 점은 변수의 개수가 시퀀스에 일치해야 한다는 것뿐이다.


## 예1)
p = (4, 5)
x, y = p
print("x : ", x)
print("y : ", y)

## 예2)
data = ['ACME', 50, 91.1, (2018, 3, 14)]
name, shares, price, date = data
print("name : ", name)
print("date : ", date)

name, shares, price, (year, mon, day) = data
print("name : %s" % name)
print("date : ", date)
print("year : ", year)
print("mon : ", mon)
print("day : ", day)

## 요소 개수가 일치하지 않으면 에러가 발생한다,
# p = (4, 5)
# x, y, z = p


### [토론] 언패킹(unpacking)은 사실 튜플이나 리스트뿐만 아니라 순환 가능한 모든 객체에 적용할 수 있다.
###        문자열, 파일, 이터레이터(iterator), 제너레이터(generator)가 포함된다.

## 예3)
s = "Hello"
a, b, c, d, e = s
print("a : ", a)
print("e : ", e)


### [내 생각] 이렇게 하면 되지 않을까?   -> "name, shares, price, date = data" 이렇게 표현하는 게 나아 보이기도 하네
data = ['ACME', 50, 91.1, (2018, 3, 14)]
name = data[0]
shares = data[1]
price = data[2]
date = data[3]
print("name : ", name)
print("date : ", date)