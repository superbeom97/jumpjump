## [ver1] 실시간 날씨 정보 request 날리는 코드
## [ver2] 스마트홈 장비 제어 프로그램
## [ver3] 인공지능 모드 ON -> 장비 제어
## [ver4] 시뮬레이션 추가
## [ver5] 창문/가습기/제습기 작동 조건을 평균이 아닌 가장 가까운 예보 시간을 기준으로 함
##        json 파일을 불러오는(읽는) 코드를 함수로 묶음
##        제습기 작동 범위 55 <= humidity_status_num <= 70 추가
##        기온을 받아 난방기 or 에어컨 작동
##        함수 이름 정리
##        통합대기환경 정보(대기오염정보 조회 서비스) json 파일로 불러오기 -> 통합대기환경 / 미세먼지 정보 이용
## [ver6 ~] -> DeviceControl_HomeNetwork.py

import urllib.request
import datetime
import time
import json
import threading

g_Radiator = False              ## 난방기
g_Airconditioner = False        ## 에어컨
g_Humidifier = False            ## 가습기
g_Dehumidifier = False          ## 제습기
g_Gas_Valve = False             ## 가스밸브
g_Balcony_Windows = False       ## 발코니(베란다) 창문
g_Door = False                  ## 출입문
g_AI_Mode = False               ## 인공지능 모드

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
json_weather_result = []
json_atmosphere_result = []
yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time()))
day_time = time.strftime("%H%M", time.localtime(time.time()))
day_hour = time.strftime("%H", time.localtime(time.time()))
day_min = time.strftime("%M", time.localtime(time.time()))
last_thrid = "30"       ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
x_coodinate = "89"      ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
y_coodinate = "91"      ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
numofrows = "100"       ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
sidoname = "대구"       ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 request 날릴 때, 항목
ver_info = "1.3"        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 request 날릴 때, 항목


def Print_Device_fir_Status(device_name, devcie_status):    ## 장비 상태 출력 함수 1-1
    print(">> %s 상태: " % device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def Print_Device_snd_Status(device_name, devcie_status):    ## 장비 상태 출력 함수 1-2
    print(">> %s 상태: " % device_name, end="")
    if devcie_status == True: print("열림")
    else: print("닫힘")

def Check_Device_Status():      ## 장비 상태 확인 함수
    print("")
    print("===================================")
    Print_Device_fir_Status('난방기', g_Radiator)
    Print_Device_fir_Status('에어컨', g_Airconditioner)
    Print_Device_fir_Status('가습기', g_Humidifier)
    Print_Device_fir_Status('제습기', g_Dehumidifier)
    Print_Device_snd_Status('가스밸브', g_Gas_Valve)
    Print_Device_snd_Status('발코니(베란다) 창문', g_Balcony_Windows)
    Print_Device_snd_Status('출입문', g_Door)
    print("===================================")
    print("")

def Control_Device():       ## 장비 제어 함수
    global  g_Radiator, g_Airconditioner, g_Humidifier, g_Dehumidifier, g_Gas_Valve, g_Balcony_Windows, g_Door      ## 전역 변수를 비교나 어사인 하려면 함수 안에서 설정해 줘야 해!!
    Check_Device_Status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 에어컨\n3. 가습기\n4. 제습기\n5. 가스밸브\n6. 발코니(베란다)창\n7. 출입문\n-> "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
    elif menu_num == 2:
        g_Airconditioner = not g_Airconditioner
    elif menu_num == 3:
        g_Humidifier = not g_Humidifier
    elif menu_num == 4:
        g_Dehumidifier = not g_Dehumidifier
    elif menu_num == 5:
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 6:
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 7:
        g_Door = not g_Door
    print("")

    Check_Device_Status()

def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
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

def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s.json' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    return day_min_int

def Read_Weather_Json():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일을 불러오는(읽는) 함수
    total_weather = []
    with open("동구_신암동_초단기예보조회_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_weather = json.loads(json_string)

    return total_weather

def get_Atmosphere_URL():   ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) request 보내기 전, url 만드는 함수

    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey=" + access_key
    parameters += "&sidoName=" + urllib.parse.quote(sidoname)
    parameters += "&ver=" + ver_info

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Atmosphere_Json():  ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Atmosphere_URL()

    for prn_data in jsonData['list']:
        if prn_data.get('stationName') == '신암동':
            json_atmosphere_result.append({'stationName':prn_data.get('stationName'),
                           'dataTime':prn_data.get('dataTime'),
                           'pm10Value':prn_data.get('pm10Value'),       ## 10μm 이하의 미세먼지를 기준으로
                           'pm10Grade1h':prn_data.get('pm10Grade1h'),
                           'khaiValue':prn_data.get('khaiValue'),
                           'khaiGrade':prn_data.get('khaiGrade')})

    with open('동구_신암동_통합대기환경정보_%s.json' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_atmosphere_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_통합대기환경정보_%s.json SAVED' % yyyymmdd)

def Read_Atmosphere_Json():        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일을 불러오는(읽는) 함수
    total_atmosphere = []
    with open("동구_신암동_통합대기환경정보_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_atmosphere = json.loads(json_string)

    return total_atmosphere

def Update_Scheduler():     ## 인공지능 모드 ON일 경우, 매 시 45분 10초 마다 실시간 정보를 업데이트 하도록 하는 함수
    while True:
        if g_AI_Mode == False:
            continue
        else:
            if time.strftime("%M%S", time.localtime(time.time())) == "4510":
                get_Realtime_Weather_Info()
                time.sleep(5)

def Control_Devices_AI(total_weather):        ## 인공지능 - 장비 제어 함수
    global g_Radiator, g_Airconditioner, g_Balcony_Windows, g_Humidifier, g_Dehumidifier

    print("===============================================================================")

################################### 난방기 / 에어컨 인공지능 모드
    temperature_num = 0     ## 난방기 / 에어컨 인공지능 모드
    for temper in total_weather:
        if temper.get('category') == "T1H":     ## 항목(category)이 온도(T1H)이면
            temperature_num += temper.get('fcstValue')
            break

    print(" 현재 기온 : %s ℃ ".center(70) % temperature_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 난방기 작동 범위 : \n     1. 기온이 15도 미만\n     2. 기온이 15도 이상 20이하일 때, 이미 난방기가 작동 중인 상황")
    print("* 에어컨 작동 범위 : 기온이 33도 이상")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 난방기 작동
    ## 겨울철 실내 적정 온도 : 18 ~ 20도
    if temperature_num < 15:    ## 기온이 15도 미만이면 난방기를 켜라
        if g_Radiator == True:  ## 난방기가 켜져 있으면, 그대로 유지
            print("기온이 15℃ 미만입니다. 작동 중인 난방기 상태를 유지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == True: print("작동\n")
        else:   ## 난방기가 꺼져 있으면, 켜라
            g_Radiator = not g_Radiator
            print("기온이 15℃ 이하입니다. 정지된 난방기를 작동합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == True: print("작동\n")

    elif 15 <= temperature_num <= 20:       ## 기온이 15도 이상 20도 이하면 현재 난방기 상태 유지
        print("기온이 적정하여 현재 난방기 상태를 유지합니다:)")
        print(">> 난방기 상태 : ", end="")
        if g_Radiator == True: print("작동\n")
        else: print("정지\n")

    elif temperature_num > 20:      ## 기온이 20도 이상이면 난방기를 꺼라
        if g_Radiator == True:  ## 난방기가 켜져 있으면, 꺼라
            g_Radiator = not g_Radiator
            print("기온이 20℃ 초과입니다. 작동 중인 난방기를 정지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == False: print("정지\n")
        else:   ## 난방기가 꺼져 있으면, 그대로 유지
            print("기온이 20℃ 초과입니다. 정지된 난방기 상태를 유지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == False: print("정지\n")

    ################## 에어컨 작동
    if temperature_num >= 33:   ## 기온이 33도 이상이면 에어컨을 켜라
        if g_Airconditioner == True:    ## 에어컨이 켜져 있으면, 그대로 유지
            print("기온이 33℃ 초과입니다. 작동 중인 에어컨 상태를 유지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == True: print("작동\n")
        else:   ## 에어컨이 꺼져 있으면, 켜라
            g_Airconditioner = not g_Airconditioner
            print("기온이 33℃ 초과입니다. 정지된 에어컨을 작동합니다.")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == True: print("작동\n")
    else:       ## 기온이 33도 미만이면 에어컨을 꺼라
        if g_Airconditioner == True:    ## 에어컨이 켜져 있으면, 꺼라
            g_Airconditioner = not g_Airconditioner
            print("기온이 33℃ 미만입니다. 작동 중인 에어컨을 정지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == False: print("정지\n")
        else:   ## 에어컨이 꺼져 있으면, 그대로 유지
            print("기온이 33℃ 미만입니다. 정지된 에어컨 상태를 유지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == False: print("정지\n")


################################### 창문 인공지능 모드
    window_status_num = 0
    for window_status in total_weather:
        if window_status.get('category') == "PTY":      ## 항목(category)이 강수형태(PTY)이면
            window_status_num += window_status.get('fcstValue')     ## 강수 형태 (없음(0), 비(1), 비/눈(2), 눈(3))
            break

    if g_Radiator == True:  ## 난방기가 작동 중이라면(강수 확률과는 상관 없이), 창문을 닫아라
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
            print("난방기가 작동 중입니다. 열린 창문을 닫습니다:)")
            print(">> 발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 창문이 닫혀 있으면
            print("난방기가 작동 중입니다. 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
            print(">> 발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == False: print("닫힘\n")

    else:   ## 난방기가 작동 중이지 않고 + 강수 확률이 있을 경우
        if window_status_num > 0:  ## 강수 확률이 있으면 창문을 닫아라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("강수 확률이 있어 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            else:  ## 창문이 닫혀 있으면
                print("강수 확률이 있어 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 강수 확률이 없으면 창문을 열어라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                print("햇살이 좋아 열린 창문 상태를 유지합니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")
            elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
                g_Balcony_Windows = not g_Balcony_Windows
                print("햇살이 좋아 닫힌 창문을 엽니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")

################################### 가습기 / 제습기 인공지능 모드
    humidity_status_num = 0
    for humidity_status in total_weather:
        if humidity_status.get('category') == "REH":     ## 항목(category)이 습도(REH)이면
            humidity_status_num += humidity_status.get('fcstValue')     ## 습도
            break

    print("====================".center(72))
    print(" 현재 습도 : %s %% ".center(70) % humidity_status_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 가습기 작동 범위 : 습도 45% 미만")    ## 실내 적정 습도 : 45 ~ 55%
    print("* 제습기 작동 범위 : \n     1. 습도가 55% 초과 70% 미만일 때, 이미 제습기가 작동 중인 상황\n     2. 습도 70% 이상")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 가습기 작동
    if humidity_status_num < 45:  ## 습도가 45% 미만이면 가습기를 켜라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            g_Humidifier = not g_Humidifier  ## 가습기 켜라
            print("습도가 45%% 미만입니다. 정지된 가습기를 작동합니다:)")
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")
        else:  ## 가습기가 켜져 있으면
            print("습도가 45%% 미만입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")

    elif humidity_status_num >= 45:   ## 습도가 45% 이상이면 가습기를 꺼라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            print("습도가 45%% 이상입니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")
        else:  ## 가습기가 켜져 있으면
            g_Humidifier = not g_Humidifier
            print("습도가 45%% 이상입니다. 작동 중인 가습기를 정지합니다:)")  ## 가습기를 꺼라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")

    ################## 제습기 작동
    if humidity_status_num <= 55:      ## 습도가 55% 이하면 제습기를 꺼라
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            print("습도가 55%% 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")
        else:  ## 제습기가 켜져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("습도가 55%% 이하입니다. 작동 중인 제습기를 정지합니다:)")  ## 제습기를 꺼라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")

    elif 55 < humidity_status_num < 70:      ## 습도가 55% 초과 70% 미만이면 제습기 상태를 그대로 유지
        print("습도가 적정하여 현재 제습기 상태를 유지합니다:)")
        print(">> 제습기 상태 : ", end="")
        if g_Dehumidifier == True: print("작동\n")    ## 켜져 있으면 그대로 켜 놓고
        else: print("정지\n")     ## 꺼져 있으면 그대로 꺼 놓고

    elif humidity_status_num >= 70:      ## 습도가 70% 이상이면 제습기를 켜라
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("습도가 70%% 이상입니다. 정지된 제습기를 작동합니다:)")  ## 제습기를 켜라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")
        else:  ## 제습기가 켜져 있으면
            print("습도가 70%% 이상입니다. 작동 중인 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")

    print("===============================================================================")

def Devices_AI():   ## 실시간 업데이트 정보 request -> json 파일 만들고 -> 장비 제어하는 함수
    get_Realtime_Weather_Info()

    if 30 < get_Realtime_Weather_Info() <= 59:  ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
                                                ## get_Realtime_Weather_Info() 하면 return -> day_min_int
        total_weather = Read_Weather_Json()  ## json 파일을 불러오는 함수 - 인공지능 모드를 위해 json 파일의 정보를 읽어 오는

        Control_Devices_AI(total_weather)   ## 장비 제어 함수

    elif 0 <= get_Realtime_Weather_Info() <= 30:  ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid

        total_weather = Read_Weather_Json()  ## json 파일을 불러오는 함수 - 인공지능 모드를 위해 json 파일의 정보를 읽어 오는

        Control_Devices_AI(total_weather)   ## 장비 제어 함수

def Smart_Mode():       ## 스마트 모드 메뉴 함수
    global g_AI_Mode
    print("<<스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 상태 변경\n3. 실시간 기상정보 Update\n-> "))

    if menu_num == 1:
        print("\n===============================")
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        print("===============================\n")

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

        ## 실시간 정보 업데이트를 하는데, 인공지능 모드가 ON인 경우, 실시간 정보 업데이트 한 것을 토대로, 상황 분석 -> 장비 제어
        if g_AI_Mode == True:
            total_weather = Read_Weather_Json()  ## json 파일을 불러오는 함수

            Control_Devices_AI(total_weather)  ## 장비 제어 함수

    print("")

def Simulation_Mode():      ## 시뮬레이션 모드 메뉴
    global g_Balcony_Windows, g_Humidifier, g_Dehumidifier
    print("<<시뮬레이션 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 비오는 날 시뮬레이션\n2. 건조한 날 시뮬레이션\n3. 습한 날 시뮬레이션\n"
                         "4. 상쾌한 날 시뮬레이션\n-> "))

    get_Realtime_Weather_Info()     ## json 파일 만들기 전 함수

    total_weather = Read_Weather_Json()     ## json 파일을 불러오는 함수

################################### 비오는 날 시뮬레이션
    if menu_num == 1:
        window_status_num = 0   ## 창문 인공지능 모드
        for window_status in total_weather:
            if window_status.get('category') == "PTY":
                window_status_num += window_status.get('fcstValue')
                break
        window_status_num = 0

        if window_status_num == 0:  ## 강수 확률이 있으면 창문을 닫아라
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

################################### 건조한 날 시뮬레이션
    elif menu_num == 2:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num < 45:  ## 평균 습도가 45% 이하면 가습기를 켜라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                g_Humidifier = not g_Humidifier  ## 가습기 켜라
                print("현재 습도가 낮습니다. 가습기를 작동시킵니다:)")
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")
            else:  ## 가습기가 켜져 있으면
                print("현재 습도가 낮습니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")

        elif humidity_status_num >= 45 and humidity_status_num <= 55:
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

        elif humidity_status_num > 55:  ## 평균 습도가 55% 이상이면 가습기를 꺼라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

################################### 습한 날 시뮬레이션
    elif menu_num == 3:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 75
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num > 70:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("습도가 높습니다. 제습기를 작동시킵니다:)")  ## 제습기를 켜라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")
            else:  ## 제습기가 켜져 있으면
                print("습도가 높습니다. 작동된 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")

        elif humidity_status_num < 55:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("습도가 제습기 작동 범위 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("습도가 제습기 작동 범위 이하입니다. 제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")

################################### 상쾌한 날 시뮬레이션
    elif menu_num == 4:
        humidity_status_num = 0   ## 가습기 / 제습기 인공지능 모드
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 50

        if 45 <= humidity_status_num and humidity_status_num <= 55:
            print("\n현재 습도 : %s%%\n" % humidity_status_num)
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