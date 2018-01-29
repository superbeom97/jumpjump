## [ver1] 실시간 날씨 정보 request 날리는 코드

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
def getWeatherURL(yyyymmdd, day_time, x_coodinate, y_coodinate):

    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "?base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate


    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_weather_info():
    access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
    jsonResult = []
    yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time()))
    day_time = time.strftime("%H%M", time.localtime(time.time()))
    x_coodinate = "89"
    y_coodinate = "91"

    jsonData = getWeatherURL(yyyymmdd, day_time, x_coodinate, y_coodinate)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']:
            jsonResult.append({'baseDate':prn_data.get('baseDate'),
                               'baseTime':prn_data.get('baseTime'),
                               'category':prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx':prn_data.get('nx'),
                               'ny':prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s_%s.json' % (yyyymmdd, day_time), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED' % (yyyymmdd, day_time))

if __name__ == '__main__':
    get_realtime_weather_info()