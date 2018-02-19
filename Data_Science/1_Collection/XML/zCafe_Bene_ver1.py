print("STRAT~~")
import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from pandas import DataFrame                ## HTML로 바꾼 코드를 테이블을 만들어 csv 파일로 저장해라
import xml.etree.ElementTree as ET

store_result = []
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

CafeBene_table = DataFrame(store_result, columns=('store_name','store_address','store_tel'))
CafeBene_table.to_csv("CafeBene_table.csv", encoding="cp949", mode='w', index=True)

print("END!!!!!")