import re

p = re.compile('[a-z]+')
m = p.findall("pythons python!!")
for z in m:
    print(type(z))
# result = p.findall("life is too short")
# result = p.finditer("life is too short")
# print(result)
# for z in result:
#     print(z)
#     print(type(z))
# if m:
#     print('Match found :', m.group())
# else:
#     print('No match')