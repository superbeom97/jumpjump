#################### 그룹핑

import re

p = re.compile('(ABC)+')
m = p.search("ABCABC")

print(m)