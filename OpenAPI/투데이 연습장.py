## [ver1] 실시간 날씨 정보 request 날리는 코드
## [ver2] 스마트홈 장비 제어 프로그램
## [ver3] 인공지능 모드 ON -> 장비 제어
## [ver4] 시뮬레이션 추가

import urllib.request
import datetime
import time
import json
import threading

g_Radiator = False              ## 난방기
g_Humidifier = False            ## 가습기
g_Dehumidifier = False          ## 제습기
g_Gas_Valve = False             ## 가스밸브
g_Balcony_Windows = False       ## 발코니(베란다) 창문
g_Door = False                  ## 출입문
g_AI_Mode = False               ## 인공지능 모드


access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
jsonResult = []
yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time()))
day_time = time.strftime("%H%M", time.localtime(time.time()))
day_hour = time.strftime("%H", time.localtime(time.time()))
day_min = time.strftime("%M", time.localtime(time.time()))
last_thrid = "30"
x_coodinate = "89"
y_coodinate = "91"
numofrows = "100"


def Print_Device_fir_Status(device_name, devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def Print_Device_snd_Status(device_name, devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True: print("열림")
    else: print("닫힘")

def Check_Device_Status():
    print("")
    print("===================================")
    Print_Device_fir_Status('난방기', g_Radiator)
    Print_Device_fir_Status('가습기', g_Humidifier)
    Print_Device_fir_Status('제습기', g_Dehumidifier)
    Print_Device_snd_Status('가스밸브', g_Gas_Valve)
    Print_Device_snd_Status('발코니(베란다) 창문', g_Balcony_Windows)
    Print_Device_snd_Status('출입문', g_Door)
    print("===================================")
    print("")

def Control_Device():
    global  g_Radiator, g_Humidifier, g_Dehumidifier, g_Gas_Valve, g_Balcony_Windows, g_Door      ## 전역 변수를 비교나 어사인 하려면 함수 안에서 설정해 줘야 해!!
    Check_Device_Status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 가습기\n3. 제습기\n4. 가스밸브\n5. 발코니(베란다)창\n6. 출입문\n-> "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
    elif menu_num == 2:
        g_Humidifier = not g_Humidifier
    elif menu_num == 3:
        g_Dehumidifier = not g_Dehumidifier
    elif menu_num == 4:
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 5:
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 6:
        g_Door = not g_Door
    print("")

    Check_Device_Status()

def get_Request_URL(url):
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

def get_WeatherURL(day_time):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=" + numofrows

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weater_Json(day_time):
    jsonData = get_WeatherURL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            jsonResult.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s.json' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():
    # 인공지능 모드가 ON인 경우에 실시간 정보를 분석하여 장비를 제어 할 조건이 된다면
    # 장비를 제어한다.
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weater_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weater_Json(day_time)

    return day_min_int

def Update_Scheduler():
    while True:
        if g_AI_Mode == False:
            continue
        else:
            if time.strftime("%M%S", time.localtime(time.time())) == "4510":
                get_Realtime_Weather_Info()
                time.sleep(5)

def Print_Devices_AI(total_weather):
    global g_Balcony_Windows, g_Humidifier, g_Dehumidifier

    window_status_ls = []  ## 창문 인공지능 모드
    window_status_num = 0
    for window_status in total_weather:
        if window_status.get('category') == "PTY":
            window_status_ls.append(window_status.get('fcstValue'))
            window_status_num += window_status.get('fcstValue')
    window_average = window_status_num / len(window_status_ls)

    if window_average > 0:  ## 강수 확률이 있으면 창문을 닫아라
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
            print("강수 확률이 있어 창문을 닫습니다:)")
            print("발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 창문이 닫혀 있으면
            print("강수 확률이 있어 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
            print("발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == False: print("닫힘\n")
    else:  ## 강수 확률이 없으면 창문을 열어라
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            print("햇살이 좋아 열린 창문 상태를 유지합니다:)")
            print("발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == True: print("열림\n")
        elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
            g_Balcony_Windows = not g_Balcony_Windows
            print("햇살이 좋아 창문을 엽니다:)")
            print("발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == True: print("열림\n")

    humidifier_status_ls = []  ## 가습기 / 제습기 인공지능 모드
    humidifier_status_num = 0
    for humidity_status in total_weather:
        if humidity_status.get('category') == "REH":
            humidifier_status_ls.append(humidity_status.get('fcstValue'))
            humidifier_status_num += humidity_status.get('fcstValue')
    humidity_average = humidifier_status_num / len(humidifier_status_ls)
    print("==========================")
    print("현재 습도 : %s%%".center(20) % humidity_average)
    print("==========================")

    if humidity_average < 45:  ## 평균 습도가 45% 이하면 가습기를 켜라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            g_Humidifier = not g_Humidifier  ## 가습기 켜라
            print("가습기를 작동시킵니다:)")
            print("가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")
        else:  ## 가습기가 켜져 있으면
            print("작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
            print("가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")

    elif humidity_average >= 45 and humidity_average <= 55:
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            print("작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
            print("가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")
        else:  ## 가습기가 켜져 있으면
            g_Humidifier = not g_Humidifier
            print("가습기를 정지시킵니다:)")  ## 가습기를 꺼라
            print("가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")

    elif humidity_average > 55:  ## 평균 습도가 55% 이상이면 가습기를 꺼라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            print("정지된 가습기를 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
            print("가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")
        else:  ## 가습기가 켜져 있으면
            g_Humidifier = not g_Humidifier
            print("가습기를 정지시킵니다:)")  ## 가습기를 꺼라
            print("가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")

    if humidity_average > 70:
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("제습기를 작동시킵니다:)")  ## 제습기를 켜라
            print("제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")
        else:  ## 제습기가 켜져 있으면
            print("작동 중인 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
            print("제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")

    elif humidity_average < 55:
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            print("정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
            print("제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")
        else:  ## 제습기가 켜져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("제습기를 정지시킵니다:)")  ## 제습기를 꺼라
            print("제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")

def Devices_AI():
    get_Realtime_Weather_Info()

    if 30 < get_Realtime_Weather_Info() <= 59:  ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
                                                ## get_Realtime_Weather_Info() 하면 return -> day_min_int
        total_weather = []      ## 인공지능 모드를 위해 json 파일의 정보를 읽어 오는
        with open("동구_신암동_초단기예보조회_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            total_weather = json.loads(json_string)
        Print_Devices_AI(total_weather)

    elif 0 <= get_Realtime_Weather_Info() <= 30:  ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid
        total_weather = []  ## 인공지능 모드를 위해 json 파일의 정보를 읽어 오는
        with open("동구_신암동_초단기예보조회_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            total_weather = json.loads(json_string)
        Print_Devices_AI(total_weather)

def Smart_Mode():
    global g_AI_Mode
    print("<<스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 상태 변경\n3. 실시간 기상정보 Update\n-> "))

    if menu_num == 1:
        print("\n현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 2:
        print("\n===============================")
        print("변경 전 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        print("===============================\n")

        if g_AI_Mode == True:
            print("<<인공지능 모드를 가동합니다>>\n".center(30))
            Devices_AI()

    elif menu_num == 3:
        get_Realtime_Weather_Info()

    print("")

def Simulation_Mode():
    global g_Balcony_Windows, g_Humidifier, g_Dehumidifier
    print("<<시뮬레이션 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 비오는 날 시뮬레이션\n2. 건조한 날 시뮬레이션\n3. 습한 날 시뮬레이션\n"
                         "4. 상쾌한 날 시뮬레이션\n-> "))

    get_Realtime_Weather_Info()

    total_weather = []
    with open("동구_신암동_초단기예보조회_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_weather = json.loads(json_string)

    if menu_num == 1:
        window_status_ls = []  ## 창문 인공지능 모드
        window_status_num = 0
        for window_status in total_weather:
            if window_status.get('category') == "PTY":
                window_status_ls.append(window_status.get('fcstValue'))
                window_status_num += window_status.get('fcstValue')
        # window_average = window_status_num / len(window_status_ls)
        window_average = 0

        if window_average == 0:  ## 강수 확률이 있으면 창문을 닫아라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("강수 확률이 있어 창문을 닫습니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            else:  ## 창문이 닫혀 있으면
                print("강수 확률이 있어 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 강수 확률이 없으면 창문을 열어라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                print("햇살이 좋아 열린 창문 상태를 유지합니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")
            elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
                g_Balcony_Windows = not g_Balcony_Windows
                print("햇살이 좋아 창문을 엽니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")

    elif menu_num == 2:
        humidifier_status_ls = []
        humidifier_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidifier_status_ls.append(humidity_status.get('fcstValue'))
                humidifier_status_num += humidity_status.get('fcstValue')
        humidity_average = humidifier_status_num / len(humidifier_status_ls)
        print("현재 습도 : %s%%" % humidity_average)

        if humidity_average < 45:  ## 평균 습도가 45% 이하면 가습기를 켜라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                g_Humidifier = not g_Humidifier  ## 가습기 켜라
                print("현재 습도가 낮습니다. 가습기를 작동시킵니다:)")
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")
            else:  ## 가습기가 켜져 있으면
                print("현재 습도가 낮습니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")

        elif humidity_average >= 45 and humidity_average <= 55:
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

        elif humidity_average > 55:  ## 평균 습도가 55% 이상이면 가습기를 꺼라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도 : %s%%" % humidity_average)
                print("현재 습도가 높습니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도 : %s%%" % humidity_average)
                print("현재 습도가 높습니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

    elif menu_num == 3:
        humidifier_status_ls = []  ## 가습기 / 제습기 인공지능 모드
        humidifier_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidifier_status_ls.append(humidity_status.get('fcstValue'))
                humidifier_status_num += humidity_status.get('fcstValue')
        # humidity_average = humidifier_status_num / len(humidifier_status_ls)
        humidity_average = 75
        print("현재 습도 : %s%%" % humidity_average)

        if humidity_average > 70:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("습도가 높습니다. 제습기를 작동시킵니다:)")  ## 제습기를 켜라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")
            else:  ## 제습기가 켜져 있으면
                print("습도가 높습니다. 작동된 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")

        elif humidity_average < 55:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("습도가 제습기 작동 범위 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("습도가 제습기 작동 범위 이하입니다. 제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")

    elif menu_num == 4:
        humidifier_status_ls = []  ## 가습기 / 제습기 인공지능 모드
        humidifier_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidifier_status_ls.append(humidity_status.get('fcstValue'))
                humidifier_status_num += humidity_status.get('fcstValue')
        # humidity_average = humidifier_status_num / len(humidifier_status_ls)
        humidity_average = 50

        if 45 <= humidity_average and humidity_average <= 55:
            print("\n현재 습도 : %s%%\n" % humidity_average)
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")


while True:
    t = threading.Thread(target=Update_Scheduler)
    t.daemon = True
    t.start()

    print("<<스마트홈 장비 관리 프로그램_ver1>>".center(30))
    menu_num = int(input("1. 장비 상태 확인\n2. 장비 제어\n3. 스마트 모드\n4. 시뮬레이션 모드\n5. 프로그램 종료\n-> "))

    if menu_num == 1:
        Check_Device_Status()
    elif menu_num == 2:
        Control_Device()
    elif menu_num == 3:
        Smart_Mode()
    elif menu_num == 4:
        Simulation_Mode()
    elif menu_num == 5:
        break