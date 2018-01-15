### 웹 스크롤링해서 매장 정보와 갯수/점유율을 2개의 파일로 따로 저장하는 버전


print("STRAT~~")
import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from pandas import DataFrame                ## HTML로 바꾼 코드를 테이블을 만들어 csv 파일로 저장해라
import xml.etree.ElementTree as ET
import csv

store_result = []
extract_result = []
max_page = 63

for page_idx in range(1, max_page+1):
    CafeBene_URL = 'http://www.caffebene.co.kr/Content/Gnb/Store/Map.aspx?code=T5M2I2&SearchValue=&gugun=&StoreName=&room=N&wifi=N&all=N&pc=N&book=N&store=N&Page=%s'%str(page_idx)

    html = urllib.request.urlopen(CafeBene_URL)
    soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

    store_name = soup.findAll('strong', attrs={'class':'storeName'})
    store_address = soup.findAll('address', attrs={'class':'addr'})
    store_tel = soup.findAll('span', attrs={'class':'tel'})

    store_address_result = []
    for store_addr in store_address:
        str_store_addr = list(store_addr)
        store_address_result.append(str_store_addr[0])

    store_tel_result = []
    for store_tl in store_tel:
        str_store_tl = list(store_tl)
        store_tel_result.append(str_store_tl[0])

    index_num = 0
    for store_nm in store_name:
        str_store_nm = list(store_nm)
        apd_address = store_address_result[index_num]
        apd_tel = store_tel_result[index_num]
        str_store_nm.append(apd_address)
        str_store_nm.append(apd_tel)
        store_result.append(str_store_nm)
        index_num += 1

Seoul_number = 0
Busan_number = 0
Daegu_number = 0
Daejeon_number = 0
Incheon_number = 0
Goangju_number = 0
Ulsan_number = 0
Jeju_number = 0
Gyeonggi_number = 0
Gangwon_number = 0
ChungcheongNorth_number = 0
ChungcheongSouth_number = 0
JeonlaNorth_number = 0
JeonlaSouth_number = 0
GyeongsangNorth_number = 0
GyeongsangSouth_number = 0

for local_nm in store_result:
    address_local = local_nm[1]
    if '서울' in address_local:
        Seoul_number += 1
    elif '부산' in address_local:
        Busan_number += 1
    elif '대구' in address_local:
        Daegu_number += 1
    elif '대전' in address_local:
        Daejeon_number += 1
    elif '인천' in address_local:
        Incheon_number += 1
    elif '광주' in address_local:
        Goangju_number += 1
    elif '울산' in address_local:
        Ulsan_number += 1
    elif '제주' in address_local:
        Jeju_number += 1
    elif '경기' in address_local:
        Gyeonggi_number += 1
    elif '강원' in address_local:
        Gangwon_number += 1
    elif '충청북도' in address_local:
        ChungcheongNorth_number += 1
    elif '충청남도' in address_local:
        ChungcheongSouth_number += 1
    elif '전라북도' in address_local:
        JeonlaNorth_number += 1
    elif '전라남도' in address_local:
        JeonlaSouth_number += 1
    elif '경상북도' in address_local:
        GyeongsangNorth_number += 1
    elif '경상남도' in address_local:
        GyeongsangSouth_number += 1

Seoul_percent = Seoul_number/len(store_result) * 100
Busan_percent = Busan_number/len(store_result) * 100
Daegu_percent = Daegu_number/len(store_result) * 100
Daejeon_percert = Daejeon_number/len(store_result) * 100
Incheon_percert = Incheon_number/len(store_result) * 100
Goangju_percert = Goangju_number/len(store_result) * 100
Ulsan_percert = Ulsan_number/len(store_result) * 100
Jeju_percert = Jeju_number/len(store_result) * 100
Gyeonggi_percert = Gyeonggi_number/len(store_result) * 100
Gangwon_percert = Gangwon_number/len(store_result) * 100
ChungcheongNorth_percert = ChungcheongNorth_number/len(store_result) * 100
ChungcheongSouth_percert = ChungcheongSouth_number/len(store_result) * 100
JeonlaNorth_percert = JeonlaNorth_number/len(store_result) * 100
JeonlaSouth_percert = JeonlaSouth_number/len(store_result) * 100
GyeongsangNorth_percert = GyeongsangNorth_number/len(store_result) * 100
GyeongsangSouth_percert = GyeongsangSouth_number/len(store_result) * 100

extract_result.append(["서울"] + ["%s개" % Seoul_number] + ["%0.2f%%" % Seoul_percent])
extract_result.append(["부산"] + ["%s개" % Busan_number] + ["%0.2f%%" % Busan_percent])
extract_result.append(["대구"] + ["%s개" % Daegu_number] + ["%0.2f%%" % Daegu_percent])
extract_result.append(["대전"] + ["%s개" % Daejeon_number] + ["%0.2f%%" % Daejeon_percert])
extract_result.append(["인천"] + ["%s개" % Incheon_number] + ["%0.2f%%" % Incheon_percert])
extract_result.append(["광주"] + ["%s개" % Goangju_number] + ["%0.2f%%" % Goangju_percert])
extract_result.append(["울산"] + ["%s개" % Ulsan_number] + ["%0.2f%%" % Ulsan_percert])
extract_result.append(["제주"] + ["%s개" % Jeju_number] + ["%0.2f%%" % Jeju_percert])
extract_result.append(["경기"] + ["%s개" % Gyeonggi_number] + ["%0.2f%%" % Gyeonggi_percert])
extract_result.append(["강원"] + ["%s개" % Gangwon_number] + ["%0.2f%%" % Gangwon_percert])
extract_result.append(["충북"] + ["%s개" % ChungcheongNorth_number] + ["%0.2f%%" % ChungcheongNorth_percert])
extract_result.append(["충남"] + ["%s개" % ChungcheongSouth_number] + ["%0.2f%%" % ChungcheongNorth_percert])
extract_result.append(["전북"] + ["%s개" % JeonlaNorth_number] + ["%0.2f%%" % JeonlaNorth_percert])
extract_result.append(["전남"] + ["%s개" % JeonlaSouth_number] + ["%0.2f%%" % JeonlaSouth_percert])
extract_result.append(["경북"] + ["%s개" % GyeongsangNorth_number] + ["%0.2f%%" % GyeongsangNorth_percert])
extract_result.append(["경남"] + ["%s개" % GyeongsangSouth_number] + ["%0.2f%%" % GyeongsangSouth_percert])


CafeBene_table = DataFrame(store_result, columns=('store_name','store_address','store_tel'))
CafeBene_table.to_csv("CafeBene_table_ver2.csv", encoding="cp949", mode='w', index=True)

Extract_CafeBene_table = DataFrame(extract_result, columns=('전국 단위별', '매장 갯수', '카페베네 점유율'))
Extract_CafeBene_table.to_csv("Extract_CafeBene_table_ver2.csv", encoding="cp949", mode='w', index=False)

print("END!!!!!")