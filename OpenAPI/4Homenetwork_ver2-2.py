## [ver1] 실시간 날씨 정보 request 날리는 코드
## [ver2] 스마트홈 장비 제어 프로그램

import urllib.request
import datetime
import time
import json
import threading

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
jsonResult = []
yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time()))
day_time = time.strftime("%H%M", time.localtime(time.time()))
check_time = time.strftime("%M%S", time.localtime(time.time()))
x_coodinate = "89"
y_coodinate = "91"
device_dic = {'g_Radiator':[g_Radiator, '난방기'], 'g_Gas_Valve':[g_Gas_Valve, '가스밸브'], 'g_Balcony_Windows':[g_Balcony_Windows, '발코니(베란다) 창문'],
              'g_Door':[g_Door, '출입문']}

def check_device_status():
    for prn_device in device_dic:
        print("%s 상태 : " % device_dic.get(prn_device)[1], end="")
        if device_dic.get(prn_device)[0] == True: print("작동")
        else: print("정지")
    print("")

def control_device():
    global  device_dic      ## 전역 변수를 비교나 어사인 하려면 함수 안에서 설정해 줘야 해!!
    check_device_status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 가스밸브\n3. 발코니(베란다)창\n4. 출입문\n-> "))

    if menu_num == 1:
        device_dic.get('g_Radiator')[g_Radiator] = not g_Radiator
    elif menu_num == 2:
        device_dic.get('g_Gas_Valve')[g_Gas_Valve] = not g_Gas_Valve
    elif menu_num == 3:
        device_dic.get('g_Balcony_Windows')[g_Balcony_Windows] = not g_Balcony_Windows
    elif menu_num == 4:
        device_dic.get('g_Door')[g_Door] = not g_Door
    print("")

    check_device_status()

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
    print("<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))

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

    with open('동구_신암동_초단기예보조회_%s.json' % (yyyymmdd), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED' % (yyyymmdd, day_time))

def update_scheduler():
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(5)
            get_realtime_weather_info()

def smart_mode():
    global g_AI_Mode
    print("<<스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(55))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 상태 변경\n3. 실시간 기상정보 Update\n"
                         "4. 강수 예보 시뮬레이션\n-> "))

    if menu_num == 1:
        print("\n현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 2:
        print("변경 전 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 3:
        get_realtime_weather_info()

    elif menu_num == 4:
        global g_Balcony_Windows
        total_weather = []
        with open("동구_신암동_초단기예보조회_%s.json" % (yyyymmdd), encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            total_weather = json.loads(json_string)

        rain_status_ls = []
        for rain_status in total_weather:
            if rain_status.get('category') == "PTY":
                rain_status_ls.append(rain_status.get('fcstValue'))
        if 1 in rain_status_ls or 2 in rain_status_ls or 3 in rain_status_ls:   ## 강수 확률이 있으면 창문을 닫아라
            for chect_rain in total_weather:
                if chect_rain.get('category') == "PTY" and chect_rain.get('fcstValue') > 0:
                    if g_Balcony_Windows == True:
                        g_Balcony_Windows = not g_Balcony_Windows
                        print("강수량이 많아 창문을 닫습니다:)")
                        print("발코니(베란다) 창문 상태 : ", end="")
                        if g_Balcony_Windows == False: print("닫힘\n")
                        return None
        else:   ## 강수 확률이 없으면 창문을 열어라
            if g_Balcony_Windows == True:   ## 창문이 열려 있으면
                print("햇살이 좋아 계속해서 창문을 열어 놓습니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")
            elif g_Balcony_Windows == False:    ## 창문이 닫혀 있으면
                g_Balcony_Windows = not g_Balcony_Windows
                print("햇살이 좋아 창문을 엽니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")

    print("")


while True:
    t = threading.Thread(target=update_scheduler)
    t.daemon = True
    t.start()

    print("<<스마트홈 장비 관리 프로그램_ver1>>".center(30))
    menu_num = int(input("1. 장비 상태 확인\n2. 장비 제어\n3. 스마트 모드\n4. 프로그램 종료\n-> "))

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        break