#################### 정규 표현식의 기초, 메타 문자!!

### 문자 클래스 []
import re

print("====== 문자 클래스 [] ======".center(30))
p = re.compile('[a-z]+')
m = p.findall("pythons python!!")
for z in m:
    print(z)

# result = p.findall("life is too short")
# result = p.finditer("life is too short")
# print(result)
# for z in result:
#     print(z)
# if result:
#     print('Match found :', result)
# else:
#     print('No match')


### Dot '.'  -  줄바꿈 문자인 \n을 제외한 모든 문자와 매치
## re.DOTALL이라는 옵션을 주면 \n을 포함하여, \n 문자와도 매치가 된다
print("")
print("====== Dot '.' ======".center(35))

p = re.compile('a.b')
m = p.match("a0b")      ## -> 매치 O : '.'이 왔으니 가운데에 어떤 문자가 와도 매치가 된다.
print(m)

p = re.compile('a[.]b')
m = p.match("a0b")      ## -> 매치 X : '[.]'이 왔으니 가운데에 string 그 자체인 '.'이 와야 매치가 된다.
print(m)                ## 매치되게 하려면 m = p.match("a.b") 가 와야 한다!


### 반복 '*'  -  '*' 바로 앞에 있는 문자가 0번 이상 반복되면 매치
print("")
print("====== 반복 '*' ======".center(33))

p = re.compile('ca*t')      ## '*' 바로 앞에 있는 'a'가 0번 이상 반복되면 매치 -> 없어도 된다!
m = p.match("ct")       ## 매치 O
n = p.match("cat")      ## 매치 O
l = p.match("caat")     ## 매치 O
print(m)
print(n)
print(l)


### 반복 '+'  -  '+' 바로 앞에 있는 문자가 1번 이상 반복되면 매치
print("")
print("====== 반복 '+' ======".center(33))

p = re.compile('ca+t')      ## '+' 바로 앞에 있는 'a'가 1번 이상 반복되면 매치 -> 'a'가 최소 1개는 와야 한다!
m = p.match("ct")       ## 매치 X
n = p.match("cat")      ## 매치 O
l = p.match("caat")     ## 매치 O
print(m)
print(n)
print(l)


### 반복 '{m,n}', '?'     -   '{}'를 사용하여 반복 횟수를 고정시킬 수 있다 // '?' = '{0,1}' 즉 '있어도 되고 없어도 된다'를 표현
## '{m,n}'  -  반복 횟수가 m부터 n까지인 것을 매치
print("")
print("====== 반복 '{m,n}' ======".center(33))

print("\n<< ca{3,}t 출력 >>")
p = re.compile('ca{3,}t')   ## {3,} : 반복 횟수가 3 이상인 경우 매치 - m 또는 n을 생략할 수도 있다
m = p.match("caat")     ## 'a'가 2개 인 경우 - 매치 X - 'a'가 3회 이상 반복되지 않아서 매치 X
n = p.match("caaat")    ## 'a'가 3개 인 경우 - 매치 O
l = p.match("caaaat")   ## 'a'가 4개 인 경우 - 매치 O
print(m)
print(n)
print(l)

print("\n<< ca{,3}t 출력 >>")
p = re.compile('ca{,3}t')   ## {,3} : 반복 횟수가 3 이하인 경우 매치 - m 또는 n을 생략할 수도 있다
m = p.match("caat")     ## 'a'가 2개 인 경우 - 매치 O
n = p.match("caaat")    ## 'a'가 3개 인 경우 - 매치 O
l = p.match("caaaat")   ## 'a'가 4개 인 경우 - 매치 X - 'a'가 3회 이하 반복되지 않아서 매치 X
print(m)
print(n)
print(l)

print("\n<< ca{2}t 출력 >>")
p = re.compile('ca{2}t')   ## {2} : 2번 반복되면 매치 - 반드시 2번 반복!!
m = p.match("cat")     ## 'a'가 1개 인 경우 - 매치 X - 'a'가 2번 반복되지 않아서 매치 X
n = p.match("caat")    ## 'a'가 2개 인 경우 - 매치 O
l = p.match("caaat")   ## 'a'가 3개 인 경우 - 매치 X - 'a'가 2회 반복되지 않아서 매치 X
print(m)
print(n)
print(l)

print("\n<< ca{2,5}t 출력 >>")
p = re.compile('ca{2,5}t')   ## {2,5} : 2~5번 반복되면 매치
m = p.match("cat")        ## 'a'가 1개 인 경우 - 매치 X - 'a'가 2~5번 반복되지 않아서 매치 X
n = p.match("caat")       ## 'a'가 2개 인 경우 - 매치 O
l = p.match("caaaaat")    ## 'a'가 5개 인 경우 - 매치 O
o = p.match("caaaaaat")   ## 'a'가 6개 인 경우 - 매치 X - 'a'가 2~5회 반복되지 않아서 매치 X
print(m)
print(n)
print(l)
print(o)

## '?' = '{0,1}' 즉 '있어도 되고 없어도 된다'를 표현
print("\n<< ab?c 출력 >>")
p = re.compile('ab?c')   ## b? : 'b'가 0~1번 사용되면 매치 -> 있어도 되고 없어도 된다!
m = p.match("ab")   ## 매치 X - 'c'가 빠져 있음
n = p.match("ac")   ## 매치 O - 'b'는 없어도 된다
l = p.match("abc")  ## 매치 O - 'b'가 있어도 된다
print(m)
print(n)
print(l)

## 응용 - 'password'와 'pw'를 동일하게 만들어 주려면?
## -> p(ass)?w(ord)?     - 'ass'가 있어도 되고 없어도 된다
print("\n<< password / pw 출력 >>")
p = re.compile('p(ass)?w(ord)?')
m = p.match("password")
n = p.match("pw")
print(m)
print(n)