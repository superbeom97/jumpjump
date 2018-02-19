######################################## 컴파일 옵션

################### DOTALL, S   -   줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
import re

p = re.compile('a.b')
m = p.match('a\nb')     ## 매치 X - '.'은 '\n'을 제외한 모든 문자와 매치되므로 -> '\n'과는 매치 X
print(m)

## 보통 re.DOTALL 옵션은 여러 줄로 이루어진 문자열에서 \n에 상관없이 검색하고자 할 때 많이 사용
print("\n<< DOTALL, S >>")
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')     ## 매치 O - re.DOTALL 옵션을 사용하면 '\n'과도 매치된다
print(m)


################### IGNORECASE, I   -   대/소문자에 관계 없이 매치할 수 있도록 한다.
print("\n<< IGNORECASE, I >>")
p = re.compile('[a-z]*', re.IGNORECASE)
m = p.match('python')
n = p.match('Python')
l = p.match('PYTHON')
print(m)
print(n)
print(l)


################### MULTILINE, M    -   여러 줄과 매치할 수 있도록 한다. (^, $ 메타 문자의 사용과 관계가 있는 옵션)
## ^ 출력
print("\n<< '^' 출력 >>")
p = re.compile("^python\s\w+")      ## '^'는 '문자열의 처음'을 의미
                                    ## '^python'은 첫 라인의 첫 단어 'python'과 매치
data = """python one
life is too short
python two
you need python
python three"""

m = p.findall(data)
print(m)

## re.MULTILINE - ^
print("\n<< MULTILINE, M - ^ : '^python\s\w+' 출력 >>")
p = re.compile("^python\s\w+", re.MULTILINE)      ## '^'는 '문자열의 처음'을 의미
                                                 ## ('^python', re.MULTILINE)은 각 라인의 첫 단어 'python'과 매치
data = """python one
life is too short
python two
you need python
python three"""

m = p.findall(data)
print(m)

## $ 출력
print("\n<< '$' 출력 >>")
p = re.compile("python\s\w+$")      ## '$'는 '문자열의 마지막'을 의미
                                    ## 'python\s\w+$'는 마지막 라인의 마지막 단어 'python\s\w+$'와 매치
data = """python one
life is too short
python two
you need python
python three"""

m = p.findall(data)
print(m)

##  re.MULTILINE - $
print("\n<< MULTILINE, M - $ >>")
p = re.compile("python\s\w+$", re.MULTILINE)      ## '$'는 '문자열의 마지막'을 의미
                                                ## ("python\s\w+$", re.MULTILINE)은 각 라인의 마지막 단어 'python\s\w+$'와 매치
data = """python one last
life is too short
before python two
you need python
python three"""

m = p.findall(data)
print(m)


################### VERBOSE, X    -    verbose 모드를 사용할 수 있도록 한다.
############### -> 정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있다.
print("\n<< Ver >>")
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);', re.VERBOSE)
m = charref.match("&#04;")
print(m)