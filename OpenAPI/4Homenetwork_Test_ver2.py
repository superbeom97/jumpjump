## [ver1] 실시간 날씨 정보 request 날리는 코드
## [ver2] 스마트홈 장비 제어 프로그램

import urllib.request
import datetime
import time
import json

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

def print_main_menu():
    print("<<스마트홈 장비 관리 프로그램_ver1>>".center(30))
    print("1. 장비 상태 확인")
    print("2. 장비 제어")
    print("3. 스마트 모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)
    print("")

def control_device():
    global  g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door      ## 전역 변수를 비교나 어사인 하려면 함수 안에서 설정해 줘야 해!!
    check_device_status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 가스밸브\n3. 발코니(베란다)창\n4. 출입문\n-> "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
    elif menu_num == 2:
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 3:
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 4:
        g_Door = not g_Door
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

def smart_mode():
    global g_AI_Mode
    print("\n<<스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(55))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 상태 변경\n3. 실시간 기상정보 Update\n-> "))

    if menu_num == 1:
        print("\n현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")

        if g_AI_Mode == True:
            while True:
                if check_time == "0815":
                    get_realtime_weather_info()
                else: continue

    elif menu_num == 3:
        get_realtime_weather_info()
    print("")


while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요 : "))
    print("")

    if (menu_num == 1):
        check_device_status()
    elif (menu_num == 2):
        control_device()
    elif (menu_num == 3):
        smart_mode()
    elif (menu_num == 4):
        break