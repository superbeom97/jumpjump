import re
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
z = p.search("park 010-1234-1234")
m = p.sub("\g<phone> \g<name>", "park 010-1234-1234")
print(z.group())
print(m)