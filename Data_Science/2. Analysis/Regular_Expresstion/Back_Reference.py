#################### 그룹핑된 문자열 재참조하기

import re

# p = re.compile(r"(\w+)\s")
# p = re.compile(r"\w+\s\w+")
# p = re.compile(r"(\w+)\s(\w+)")

p = re.compile(r"(\w+)\s\1")        ## back reference 하기 위해서는 반드시 'r'을 넣어야 한다!!
m = p.search("sdf Hello Hello ")
print(m)

p = re.compile(r"(\w+)\s(\w+)\s\1\s\2")     ## back reference 하기 위해서는 반드시 'r'을 넣어야 한다!!
m = p.search("sdf Hello World Hello World dkfjkdsfj ")
print(m)

p = re.compile(r"(\w+)\s(\w+)\s\2\s\1")
m = p.search("sdf Hello World Hello World World Hello dkfjkdsfj ")
print(m)