## py -m pip install pandas         ## pandas 설치 키워드
print("Start")
import urllib.request
import os                           ## 작성하고 있는 .py가 속해 있는 폴더에 하위폴더 생성하는 코드
from pandas import DataFrame

result = []

import xml.etree.ElementTree as ET
response = urllib.request.urlopen(
    'http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (
    urllib.parse.quote('전체'), urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name] + [store_sido] + [store_gungu] + [store_address])

nene_table = DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))

try:
    count = 1
    while True:
        try:
            f = open("D:\Python_workspace\jumpjump\XML_\V1_BigData/nene%s.csv" % count, 'r')
            data = f.read()
            count += 1
        except:
            nene_table.to_csv('V1_BigData/nene%s.csv' % count, encoding="cp949", mode='w', index=True)
            break
except:
    os.system("mkdir V1_BigData")   ## 작성하고 있는 .py가 속해 있는 폴더에 하위에 V1_BigData 폴더가 생성됨
    nene_table.to_csv('V1_BigData/nene1.csv', encoding="cp949", mode='w', index=True)

print("End")