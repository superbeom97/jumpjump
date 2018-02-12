print("START~~")
import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET

result = []
dir_name = "V4_BigData"
dir_rest = "\\"
next_dir_name = "Nene_data"
file_name = "nene"
text_name = "index_text.txt"
csv_name = ".csv"
record_limit = 3

def make_dir(dir_index):
    os.mkdir(dir_name + dir_rest + next_dir_name + str(dir_index))

def make_file(dir_index, file_index):
    make_file_name = dir_name + dir_rest + next_dir_name + str(dir_index) + dir_rest + file_name + str(file_index) + csv_name
    record_table.to_csv(make_file_name, encoding="cp949", mode='w', index=True)

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))


if os.path.isdir(dir_name):
    with open(dir_name + dir_rest + text_name, 'r') as text:
        dir_index_count = text.readline()
        dir_index_count = int(dir_index_count)
        dir_index_count += 1
        make_dir(dir_index_count)
        file_index_count = 1
        change_record_result = []
        for record_hun in result:
            change_record_result.append(record_hun)
            if len(change_record_result) > 100:
                file_index_count += 1
                record_table = DataFrame(change_record_result, columns=('store', 'sido', 'gungu', 'store_address'))
                make_file(dir_index_count, file_index_count)
                change_record_result = []
            record_table = DataFrame(change_record_result, columns=('store', 'sido', 'gungu', 'store_address'))
            make_file(dir_index_count, file_index_count)

    with open(dir_name + dir_rest + text_name, 'w') as text:
        text.write(str(dir_index_count))

elif not os.path.isdir(dir_name):
    os.mkdir(dir_name)
    with open(dir_name + dir_rest + text_name, 'w') as text:
        text.write("1")
    with open(dir_name + dir_rest + text_name, 'r') as text:
        dir_index_count = text.readline()
        dir_index_count = int(dir_index_count)
        file_index_count = 1
        make_dir(dir_index_count)
        change_record_result = []
        for record_hun in result:
            change_record_result.append(record_hun)
            if len(change_record_result) > 100:
                file_index_count += 1
                record_table = DataFrame(change_record_result, columns=('store', 'sido', 'gungu', 'store_address'))
                make_file(dir_index_count, file_index_count)
                change_record_result = []
            record_table = DataFrame(change_record_result, columns=('store', 'sido', 'gungu', 'store_address'))
            make_file(dir_index_count, file_index_count)


print("END!!!!!")