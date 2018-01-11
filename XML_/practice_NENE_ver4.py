### 미완성!!


#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
print("Start")
import urllib.request
import os
import csv
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
split_nene_result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"        ## delimiter : 구분자
nene_dir = "Nene_Data"
nene_file = "nene"
nene_origin = "origin"
csv = ".csv"
record_limit = 3

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))        ## os.mkdir 디렉터리 생성
    return None

def make_nene(dir_index, file_index) :
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + str(file_index) + csv
    nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

def make_nene_origin() :
    destination_csv = dir_name + dir_delimiter + nene_origin + csv
    nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None


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

try : os.mkdir(dir_name)
except : pass
with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
    file.write('2')
make_dir(1)
make_nene_origin()

with open("V4_BigData\\origin.csv", newline="") as infile:
    data = list(csv.reader(infile))

print("End")