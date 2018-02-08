### 출입국관광자원통계서비스에서 긁어오는
## 2016년 12월 우리나라 방문객 Top 10개국 정보 수집

import urllib.request
import datetime
import json
import math
from pprint import pprint

access_key = "9KZWqReM4nIu9eveBI1ZStRZxlUJWjTxAU2Igy32OL5au3APSLIJr8oz9NYVPKkwJnCEsOHJ04Far7N%2FfxJf2A%3D%3D"
# access_key = "svU%2Bw%2F5D%2FL7%2Fc0g4YKdOsn20gs%2BSXBxCuYXGQFL9IvIWGEQxHEXrhIM1zu%2BeqXP%2B7VIJPPvsANnm8AOgIXN2Jg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [CODE 1]
def getTourPointVisitor(yyyymm, natCd, edCd, nItems):

    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=JSon_&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + urllib.parse.quote(str(natCd))
    parameters += "&ED_CD=" + urllib.parse.quote(edCd)

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

# [CODE 2]
def getTourPointData(sort_data, yyyymm, jsonResult):
    ed = '' if 'ed' not in sort_data.keys() else sort_data['ed']
    edCd = '' if 'edCd' not in sort_data.keys() else sort_data['edCd']
    natCd = '' if 'natCd' not in sort_data.keys() else sort_data['natCd']
    natKorNm = '' if 'natKorNm' not in sort_data.keys() else sort_data['natKorNm']
    num = 0 if 'num' not in sort_data.keys() else sort_data['num']
    rnum = 0 if 'rnum' not in sort_data.keys() else sort_data['rnum']

    jsonResult.append({'yyyymm':yyyymm, 'ed':ed, 'natKorNm':natKorNm, 'num':num, 'natCd':natCd, 'edCd':edCd, 'rnum':rnum})

def main():
    jsonResult = []

    edCd = 'E'
    nPagenum = 1
    nTotal = 0
    nItems = 10000

    nSearchYear = 2016
    nSearchMonth = 12

    yyyymm = str(nSearchYear) + str(nSearchMonth)

    # [CODE 3]
    natCd = 99
    while True:
        nPage = 0
        natCd += 1
        if natCd < 1000:
            jsonData = getTourPointVisitor(yyyymm, natCd, edCd, nItems)

            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                nTotal = jsonData['response']['body']['totalCount']

                if nTotal == 0:
                    continue

                sort_data = jsonData['response']['body']['items']['item']
                getTourPointData(sort_data, yyyymm, jsonResult)

                nPage = math.ceil(nTotal/100)

            else:
                break

    jsonResult.sort(key=lambda x: x['num'], reverse=True)

    with open('전 세계_방문객_%d_%d.JSon_' % (nSearchYear, nSearchMonth), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('전 세계_방문객_%d_%d.JSon_ SAVED' % (nSearchYear, nSearchMonth))
    pprint(jsonResult)

if __name__ == '__main__':
    main()