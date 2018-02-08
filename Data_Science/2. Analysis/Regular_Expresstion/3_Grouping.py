######################################## 그룹핑 - 그룹을 만들어 주는 ()
import re

print("\n<< (ABC)+ 출력 >>")
p = re.compile('(ABC)+')    ## ABC라는 문자열이 계속해서 반복되는지 알아보고 싶다면?
m = p.search("ABCABCABC OK?")
print(m)
## >> <_sre.SRE_Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())    ## 매치된 문자열을 리턴
## >> ABCABCABC
print(m.group(0))   ## 매치된 전체 문자열을 리턴
## >> ABCABCABC
print(m.group(1))   ## 첫 번째 그룹에 해당되는 문자열을 리턴
## >> ABC

############### 응용
print("\n<< r'\w+\s+\d+[-]\d+[-]\d+' 출력 >>")            ## 이름과 전화번호를 하나의 문자열로밖에 못 받아
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group())

## << 그럼 이렇게 매치된 문자열 중에서 이름만 뽑아내고 싶다면 어떻게 해야 할까? >>
## -> 그룹핑!! 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위해서!
## '\w+' 부분을 그룹 '(\w+)'으로 만들면 group(인덱스)를 이용하여, 그룹핑된 부분의 문자열만 뽑아낼 수 있다.

###### '이름' 부분만 뽑고 싶다면?
print("\n<< r'(\w+)\s+\d+[-]\d+[-]\d+' 출력 >>")
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")      ## '이름' 부분만 그룹핑
m = p.search("park 010-1234-1234")
print(m.group())        ## park 010-1234-1234
print(m.group(0))       ## park 010-1234-1234
print(m.group(1))       ## park

###### '이름' 부분과 '전화번호' 부분을 뽑고 싶다면?
print("\n<< r'(\w+)\s+(\d+[-]\d+[-]\d+)' 출력 >>")
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")        ## '이름' 부분과 '전화번호' 부분을 각각 그룹핑
m = p.search("park 010-1234-1234")
print(m)                ## >> <_sre.SRE_Match object; span=(0, 18), match='park 010-1234-1234'>
print(m.group())        ## >> park 010-1234-1234
print(m.group(1))       ## >> park
print(m.group(2))       ## >> 010-1234-1234

###### '전화번호' 부분에서 '국번'만 뽑아내고 싶다면?
print("\n<< r'(\w+)\s+((\d+)[-]\d+[-]\d+)' 출력 >>")
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")        ## '전화번호' 부분에서 '국번' 부분을 그룹핑 - 그룹을 중첩되게 사용 가능
m = p.search("park 010-1234-1234")                     ## 그룹이 중첩되어 있는 경우 바깥에서 안쪽으로 들어갈수록 인덱스 증가
print(m)                ## >> <_sre.SRE_Match object; span=(0, 18), match='park 010-1234-1234'>
print(m.group())        ## >> park 010-1234-1234
print(m.group(1))       ## >> park
print(m.group(2))       ## >> 010-1234-1234
print(m.group(3))       ## >> 010