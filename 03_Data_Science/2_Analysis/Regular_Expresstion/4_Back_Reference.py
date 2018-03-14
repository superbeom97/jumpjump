######################################## 그룹핑된 문자열 재참조하기
######## 그룹의 또 하나 좋은 점 - 한번 그룹핑된 문자열을 재참조할 수 있다는 점
import re

print("<< 'Paris in the the spring' 출력 >>")
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring')
print(m.group())    ## >> the the

print("\n<< 'sdf Hello Hello ' 출력 >>")
p = re.compile(r"(\w+)\s\1")        ## back reference 하기 위해서는 반드시 'r'을 넣어야 한다!!
m = p.search('sdf Hello Hello ')
print(m.group())    ## >> Hello Hello

print("\n<< 'sdf Hello World Hello World dkfjkdsfj ' 출력 >>")
p = re.compile(r"(\w+)\s(\w+)\s\1\s\2")     ## back reference 하기 위해서는 반드시 'r'을 넣어야 한다!!
m = p.search('sdf Hello World Hello World dkfjkdsfj ')
print(m.group())    ## >> Hello World Hello World

print("\n<< 'sdf Hello World Hello World World Hello dkfjkdsfj ' 출력 >>")
p = re.compile(r"(\w+)\s(\w+)\s\2\s\1")
m = p.search("sdf Hello World Hello World World Hello dkfjkdsfj ")
print(m.group())    ## >> Hello World World Hello