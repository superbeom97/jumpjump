#################### 그룹핑된 문자열에 이름 붙이기   -   ?P<name>
import re

print("<< 첫번째 그룹 이름 활용 >>")
p = re.compile(r"(?P<greeting>\w+)\s\1")
m = p.search("sdf Hello Hello ")
print(m)
print(m.group())
print(m.group("greeting"))

print("\n<< 두번째 그룹 이름 활용 >>")
p = re.compile(r"(?P<greeting>\w+)\s(?P<destination>\w+)\s\1\s\2")
m = p.search("sdf Hello World Hello World dkfjkdsfj ")
print(m)
print(m.group())
print(m.group("greeting"))
print(m.group("destination"))

print("\n<< ?P<name> 사용하여 그룹핑된 문자열에 이름 붙이고, 이름으로 그룹 참조하기 >>")
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")      ## ?P<name> 사용하여 그룹핑된 문자열에 이름 붙이기
m = p.search("park 010-1234-1234")
print(m.group('name'))  ## >> park

print("\n<< 그룹명을 이용하여 정규식 내에서 재참조하기 >>")
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")              ## (?P=그룹명) 사용하여 그룹 재참조하기
m = p.search('Paris in the the spring')
print(m.group())