#################### 전방 탐색

import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
## >> http:

p = re.compile(".+(?=:)")   ## ':'는 소모되지 않는다. -> 즉 제외해라
m = p.search("http://google.com")
print(m.group())
## >> http      # ':'는 소모되지 않는다 = 빼라