######################################## 메타 문자

###################     |   -   or과 동일한 의미로 사용 -> A|B = 'A 또는 B'라는 의미
import re

print("<< '|'에 대해 알아보자 >>")
p = re.compile("Crow|Servo")
m = p.match('CrowHello')
print(m)

###################     ^   -   문자열의 맨 처음과 매치함을 의미
print("\n<< '^'에 대해 알아보자 >>")
                                                ## '^Life'는 Life라는 문자열이 처음에 온 경우에만 매치
print(re.search('^Life', 'Life is too short'))  ## 매치 O
print(re.search('^Life', 'My Life'))            ## 매치 X

###################     $   -   문자열의 끝과 매치함을 의미 - '^'와 반대의 경우
print("\n<< '$'에 대해 알아보자 >>")
print(re.search('short$', 'Life is too short'))                     ## 매치 O
print(re.search('short$', 'Life is too short, you need python'))    ## 매치 X
#### ^ 또는 $ 문자를 메타 문자가 아닌, 문자 그 자체로 매치하고 싶은 경우에는 [^], [$]처럼 사용하거나 \^, \$로 사용하면 된다.

###################     \A   -   문자열의 처음과 매치됨을 의미
### ^ 메타 문자와 동일한 의미이지만, re.MULTILINE 옵션을 사용할 경우 다르게 해석
### re.MULTILINE 옵션을 사용 -> ^은 라인별 문자열의 처음과 매치
### re.MULTILINE 옵션을 사용 -> \A는 라인과 상관 없이 전체 문자열의 처음과 매치

###################     \Z   -   문자열의 끝과 매치됨을 의미
### $ 메타 문자와 동일한 의미이지만, re.MULTILINE 옵션을 사용할 경우 다르게 해석
### re.MULTILINE 옵션을 사용 -> $는 라인별 문자열의 끝과 매치
### re.MULTILINE 옵션을 사용 -> \Z는 라인과 상관 없이 전체 문자열의 끝과 매치


###################     \b   -   단어 구분자
print("\n<< '\\b'에 대해 알아보자 >>")
p = re.compile(r'\bclass\b')
z = re.compile('\bclass\b')             ## r을 붙이지 않으면 백스페이스를 의미
print(p.search('no class at all'))              ## 매치 O
print(p.search('the declassified at all'))      ## 매치 X - class 앞과 뒤가 공백이 아니므로
print(p.search('one subclass is'))              ## 매치 X - class 앞이 공백이 아니므로
## 백스페이스가 아닌 단어 구분자임을 알려 주기 위해 Raw string임을 알려주는 r을 반드시 붙여 주어야 한다.
