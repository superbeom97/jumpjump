### 출입국관광자원통계서비스에서 긁어오는
## 중국인 방문객 빅데이터 수집


import urllib.request
import datetime
import json
import math

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
# total_info_ls = []

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

    parameters = "?_type=json&serviceKey=" + access_key
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

    return

def main():
    jsonResult = []

    natKorNm = ''
    natCd = 0
    edCd = 'E'
    nPagenum = 1
    nTotal = 0
    nItems = 100

    nSearchYear = 2016
    nSearchMonth = 12

    yyyymm = str(nSearchYear) + str(nSearchMonth)
    nPagenum = 1

    # [CODE 3]
    while True:
        for One_of_Nat_Cd in range(100, 901):
            jsonData = getTourPointVisitor(yyyymm, natCd, edCd, nItems)

            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                nTotal = jsonData['response']['body']['totalCount']
                if nTotal == 0:
                    continue


                if jsonData['response']['body']['items']['item']['natCd']:
                    sort_data = jsonData['response']['body']['items']['item']
                    getTourPointData(sort_data, yyyymm, jsonResult)
                else: continue

            else:
                break

        nPage = math.ceil(nTotal / 100)

        if (nPagenum == nPage):
            break

        nPagenum += 1

        with open('%s인_방문객_%d_%d.json' % (natKorNm, nSearchYear, nSearchMonth), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

            outfile.write(retJson)

        print('%s인_방문객_%d_%d.json SAVED' % (natKorNm, nSearchYear, nSearchMonth))

if __name__ == '__main__':
    main()