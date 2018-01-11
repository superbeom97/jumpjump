print("START~")
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V1_BigData"
dir_rest = "\\"
file_name = "nene"
text_name = "index_count.txt"
csv_name = ".csv"

def make_dir():
    make_dir_name = dir_name
    os.mkdir(make_dir_name)
    with open(dir_name + dir_rest + text_name, 'w') as text:
        text.write("0")

def make_file():
    with open(dir_name + dir_rest + text_name, 'r') as text:
        index_count = text.readline()
        count = int(index_count) + 1
        make_file_name = dir_name + dir_rest + file_name + str("%s" % count) + csv_name
        nene_table.to_csv(make_file_name, encoding="cp949", mode='w', index=True)

    with open(dir_name + dir_rest + text_name, 'w') as text:
        text.write(str(count))

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))


while True:
    if os.path.isdir(dir_name):
        make_file()
        break
    elif not os.path.isdir(dir_name):
        make_dir()
        make_file()
        break

print("END!!!!")