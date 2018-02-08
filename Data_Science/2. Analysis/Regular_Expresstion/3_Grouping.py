######################################## 그룹핑 - 그룹을 만들어 주는 ()
import re

print("<<  >>")
p = re.compile('(ABC)+')    ## ABC라는 문자열이 계속해서 반복되는지 알아보고 싶다면?
m = p.search("ABCABC")
print(m)