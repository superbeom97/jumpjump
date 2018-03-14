#### Chapter1 - 1.2 임의 순환체의 요소 나누기
### [문제] 순환체를 언패킹하려는데 요소가 N개 이상 포함되어 "값이 너무 많습니다"라는 예외가 발생한다.
### [해결] 이 문제 해결을 위해 파이썬 "별 표현식"을 사용한다.


## 예1)   예를 들어, 학기 성적을 산출할 때 첫 번째와 마지막 과제 점수를 무시하고 나머지의 평균을 사용한다고 가정해 보자.
##        과제가 네 번 있었다면 단순히 네 개를 모두 언패킹하면 되겠지만 과제가 24개였다면 어떨까?
##        이때 별 표현식을 사용하면 편리하다.
print("<< 예1 >>\n")

def drop_first_last(grades):
    first, *middle, last = grades
    return (sum(middle)/(len(grades)-2))

grades = [85, 90, 10, 20,63, 98, 70, 79, 88, 93, 45, 54, 80, 82, 100, 100, 92]
print(drop_first_last(grades))

## 예2)
print("\n<< 예2 >>\n")

record = ('Dave', 'dave@example.com', '773-555-1235', '847-555-1212')
# record = ('Dave', 'dave@example.com')     ## *phone_numbers가 하나 이상이든 아예 없든 상관 없다.
# ↳ 이 경우 print("phone_numbers : ", phone_numbers) >> phone_numbers : []
name, email, *phone_numbers = record
print("name : ", name)
print("email : ", email)
print("phone_numbers : ", phone_numbers)

## 예3) 별표가 붙어 있는 변수가 리스트의 처음에 올 수도 있다.
## ↳ 회사의 마지막 여덟 분기 판매 지표를 담은 값이 시퀀스에 들어 있다고 하자.
##   만약 가장 최근 지표가 나머지 7번의 값과 어떻게 달라졌는지 보고 싶다면
print("\n<< 예3 >>\n")

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record
## ↳ 또는 바로 대입하면, *trailing_qtrs, current_qtr = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing_qtrs : ", trailing_qtrs)
print("current_qtr : ", current_qtr)


### [토론] 이러한 방식은 길이를 알 수 없는 순환체에 안성맞춤이다.
###        때때로 순환체에 들어 있는 패턴이나 구조(예를 들어, 1 뒤에 나오는 요소는 무조건 전화번호)를
###        가지고 있는데, 이럴 때도 별표 구문을 사용하면 좋다.

## 예4) ★ 길이가 일정하지 않은 튜플에 사용하면 편리하다.
print("\n<< 예4 >>\n")

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

## 예5) 별표는 문자열 프로세싱에 사용해도 편리하다.
print("\n<< 예5 >>\n")

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print("uname : ", uname)
print("fields : ", fields)
# print("*fields : ", *fields)
print("homedir : ", homedir)
print("sh : ", sh)

## 예6) 언패킹 이후에 특정 값을 버리고 싶다면?
print("\n<< 예6 >>\n")

data = ['ACME', 50, 91.1, (2018, 3, 14)]
name, *_, (*__, day) = data
print("name : ", name)
print("_ : ", _)
print("__ : ", __)
print("day : ", day)

## 예7) 리스타가 있을 때, 손쉽게 머리와 꼬리 부분으로 분리할 수 있다.
print("\n<< 예7 >>\n")

items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print("head : ", head)
print("tail : ", tail)
print(sum(tail))