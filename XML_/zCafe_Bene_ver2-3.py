print("STRAT~~")
import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from pandas import DataFrame                ## HTML로 바꾼 코드를 테이블을 만들어 csv 파일로 저장해라
import xml.etree.ElementTree as ET
import csv

store_result = []
extract_result = []

store_address_result = []
max_page = 63

for page_idx in range(1, max_page+1):
    CafeBene_URL = 'http://www.caffebene.co.kr/Content/Gnb/Store/Map.aspx?code=T5M2I2&SearchValue=&gugun=&StoreName=&room=N&wifi=N&all=N&pc=N&book=N&store=N&Page=%s'%str(page_idx)

    html = urllib.request.urlopen(CafeBene_URL)
    soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

    store_name = soup.findAll('strong', attrs={'class':'storeName'})
    store_address = soup.findAll('address', attrs={'class':'addr'})
    store_tel = soup.findAll('span', attrs={'class':'tel'})

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


local_count = [i[0]+i[1]+i[2] for i in store_address_result]     ## 처음 배우게 된 코드!!

Seoul_number = local_count.count("서울특")
Busan_number = local_count.count("부산광")
Daegu_number = local_count.count("대구광")
Daejeon_number = local_count.count("대전광") + local_count.count("대전시")
Incheon_number = local_count.count("인천광")
Goangju_number = local_count.count("광주광")
Ulsan_number = local_count.count("울산광")
Jeju_number = local_count.count("제주특")
Sejong_number = local_count.count("세종특")
Gyeonggi_number = local_count.count("경기도")
Gangwon_number = local_count.count("강원도")
ChungcheongNorth_number = local_count.count("충청북")
ChungcheongSouth_number = local_count.count("충청남")
JeonlaNorth_number = local_count.count("전라북")
JeonlaSouth_number = local_count.count("전라남")
GyeongsangNorth_number = local_count.count("경상북")
GyeongsangSouth_number = local_count.count("경상남")

print(Seoul_number+Busan_number+Daegu_number+Daejeon_number+Incheon_number+Goangju_number+Ulsan_number+Jeju_number+Sejong_number
      +Gyeonggi_number+Gangwon_number+ChungcheongNorth_number+ChungcheongSouth_number+JeonlaNorth_number+JeonlaSouth_number
      +GyeongsangNorth_number+GyeongsangSouth_number)
print(len(store_address_result))