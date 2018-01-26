### 출입국관광자원통계서비스에서 긁어오는
## 중국인 방문객 빅데이터 수집


import urllib.request
import datetime
import json
import math

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"

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

    natKorNm = '중국'
    natCd = 112
    edCd = 'E'
    nPagenum = 1
    nTotal = 0
    nItems = 100

    nStartYear = 2011
    nEndYear = 2017

    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            nPagenum = 1

            # [CODE 3]
            while True:
                jsonData = getTourPointVisitor(yyyymm, natCd, edCd, nItems)

                if (jsonData['response']['header']['resultMsg'] == 'OK'):
                    nTotal = jsonData['response']['body']['totalCount']

                    if nTotal == 0:
                        break

## jsonData['response']['body']['items']['item']가 Tourist_Site에서는 여러 개의 딕셔너리 셋트가 리스트로 들어와서 for문을 돌렸지만
## 여기에서는 하나의 딕셔너리로 받기 때문에 바로 getTourPointData() 함수에 넣어 줘야 하는!!
                    sort_data = jsonData['response']['body']['items']['item']
                    getTourPointData(sort_data, yyyymm, jsonResult)
                    # for item in jsonData['response']['body']['items']['item']:
                    #     getTourPointData(item, yyyymm, jsonResult)

                    nPage = math.ceil(nTotal/100)

                    if (nPagenum == nPage):
                        break

                    nPagenum += 1

                else:
                    break

    with open('%s인_방문객_%d_%d.json' % (natKorNm, nStartYear, nEndYear-1), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('%s인_방문객_%d_%d.json SAVED' % (natKorNm, nStartYear, nEndYear-1))

if __name__ == '__main__':
    main()