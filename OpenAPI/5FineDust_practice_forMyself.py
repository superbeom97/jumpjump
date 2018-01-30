## 미세먼지 request 날리는 코드

import urllib.request
import datetime
import json
import time

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
def getFineDustURL(yyyymmdd, searchdate):

    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&searchDate=" + searchdate


    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_FineDust():
    jsonResult = []
    yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time()))
    searchdate = "2018-01-29"

    jsonData = getFineDustURL(yyyymmdd, searchdate)

    if (jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.'):
        for prn_data in jsonData['response']['body']['items']['item']:
            jsonResult.append({'dataTime':prn_data.get('dataTime'),
                               'informOverall':prn_data.get('informOverall'),
                               'informCause':prn_data.get('informCause'),
                               'informGrade':prn_data.get('informGrade')})

    with open('전국_미세먼지_예보_%s.json' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('전국_미세먼지_예보_%s.json SAVED' % yyyymmdd)

if __name__ == '__main__':
    get_FineDust()