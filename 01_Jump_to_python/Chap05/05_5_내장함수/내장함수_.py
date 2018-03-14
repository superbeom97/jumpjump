# chr -> 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력
chr(97)
print(chr(97))
chr(48)
print(chr(48))

# ord -> 문자의 아스키 코드값을 리턴
ord('a')
print(ord('a'))
ord('O') # 대문자 O
print(ord('O')) # 대문자 O
print(ord('o')) # 소문자 o
print(ord('0')) # 숫자 0  숫자 0을 ord(0)으로 사용하면 안 되고 따옴표 처리해서 ord('0')으로 해야 함

# positive
def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# filter
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# lambda
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex -> 정수를 16진수로
hex(234)
print(hex(234))
hex(112453)
print(hex(112453))

# oct -> 정수를 8진수 문자열로
oct(34)
print(oct(34))
print(oct(88))
print(oct(34)+oct(88))

# id
a = 97
id(97)
print(id(a))
print(id(97))

# input
# a = input("입력하시오: ")

# int
int('10', 8) # int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환
print(int('10', 8))

# isinstance
class Person: pass

a = Person()
b = 5
isinstance(b, Person)
print(isinstance(b, Person))
print(isinstance(a, Person))

# lambda
myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList)
myList[0](3,4)
print(myList[0](3,4))
myList[1](3,4)
print(myList[1](3,4))

# map
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
# a = two_times([1,2,3,4]) 변수를 result가 아닌 임의로 정해도 상관 없다.
print(a)


def two_times(x): return x*2 # 위의 예제를 map을 사용하여

list(map(two_times, [1,2,3,4]))
print(list(map(two_times, [1,2,3,4])))


def plus_one(x):
    return x+1

print(list(map(plus_one, [6]))) # 그냥 map(plus_one, 6) 하면 안 돼 [6]으로 해줘야 하는
print(list(map(plus_one, [1,2,3,4,5])))

# pow(x, y) : x의 y 제곱한 결과값을 리턴
pow(2, 4) # 2**4와 같다
print(pow(2, 4))
print(2**4)

# sorted
a = [3, 54, 1]
print(a)
a.sort() # sort는 리스트의 요소를 순서대로 정렬해 주는 리스트 함수
print(a)
print(sorted([3,55,1])) # sorted는 바로 정렬해 주는 내장 함수

# str
a = "hi"
b = a.upper()
print(a)
print(b)

# zip : 동일한 개수로 이루어진 자료형을 묶어 준다
print(list(zip([1,2,3],['a','b','c'])))
print(list(zip([1,2,3],['a','b',a]))) # 'a', 'b'는 문자열로, a는 변수로 사용
print(list(zip([1,2,3],[a,b]))) # [a,b] 처럼 변수를 넣을 순 있지만, [e,d] 처럼 변수가 아닌
print(list(zip([1,2,3],['e','d']))) # 문자열로 넣고 싶으면 ['e','d'] 처럼 따옴표를 사용해 줘야 한다!