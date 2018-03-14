############################### 스마트 모드 - 인공지능 모드 모듈

import time
from URL_Request_Json_Read_HomeNetwork import *
from Check_Control_Device_HomeNetwork import *

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
json_weather_result = []
json_atmosphere_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
last_thrid = "30"       ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
x_coodinate = "89"      ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
y_coodinate = "91"      ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
numofrows = "100"       ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
sidoname = "대구"       ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일 request 날릴 때, 항목
ver_info = "1.3"        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일 request 날릴 때, 항목


def Update_Scheduler():     ## 인공지능 모드 ON일 경우, 매 시 45분 10초 마다 실시간 정보를 업데이트 하도록 하는 함수
    while True:
        if g_AI_Mode == False:
            continue
        else:   ## 인공지능 모드가 켜지면
            if time.strftime("%M%S") == "4510":     ## 매 시 45분 10초에
                get_Realtime_Weather_Info()     ## 실시간 기상정보를 업데이트 해라
                Make_Atmosphere_Json()          ## 실시간 대기환경정보를 업데이트 해라
                time.sleep(5)   ## 업데이트 하고는 5초간 잠재워라 -> 업데이트를 한 번만 하도록

def Window_Ventilation():   ## 환기 모드 작동 -> 2시간 창문 닫고 20분 창문 열도록(2시간마다 20분씩 창문 열어서 환기) 하는 함수
    global g_Balcony_Windows
    while True:
        if g_Ventilation_Mode == False:
            continue
        else:   ## 환기 모드가 켜지면
            if g_Balcony_Windows == False:  ## 창문이 닫혀 있다면
                g_Balcony_Windows = not g_Balcony_Windows       ## 창문을 열어라
                time.sleep(1200)    ## 20분 동안
            else:   ## 창문이 열려 있다면
                time.sleep(1200)    ## 20분 동안 창문을 열어 놔라

            g_Balcony_Windows = not g_Balcony_Windows   ## 이제 창문을 닫아라
            time.sleep(7200)        ## 2시간 동안

def Ventilation_Mode():
    global g_Ventilation_Mode
    switch_num = int(input("<< 환기 모드를 켜시겠습니까? >>\n1. ON\n2. OFF\n-> "))
    if switch_num == 1:
        print("\n===============================")
        print("환기 모드를 가동합니다:)\n")
        print(">> 변경 전 환기 모드 : ", end="")
        if g_Ventilation_Mode == False: print("정지")
        g_Ventilation_Mode = not g_Ventilation_Mode
        print(">> 현재 환기 모드 : ", end="")
        if g_Ventilation_Mode == True: print("작동")
        print("\n2시간마다 20분씩 환기")
        print("===============================\n")

    elif switch_num == 2:
        print("\n======================================")
        print("환기 모드 정지 상태를 유지합니다:)")
        print("======================================\n")


def Control_Devices_AI(total_weather, total_atmosphere):        ## 인공지능 - 장비 제어 함수
    global g_Radiator, g_Airconditioner, g_Aircleaner, g_Balcony_Windows, g_Humidifier, g_Dehumidifier

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

################################### 공기청정기 인공지능 모드
    atmosphere_num = 0
    for atmosphere_status in total_atmosphere:
        atmosphere_num += int(atmosphere_status.get('khaiValue'))        ## 통합대기환경 지수
        break

    print("================================".center(72))
    print(" 현재 통합대기환경 지수 : %s".center(60) % atmosphere_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 공기청정기 작동 범위 : 통합대기환경 지수 100 초과")  ## 통합대기환경 지수 101 ~ : 나쁨
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 공기청정기 작동
    if atmosphere_num > 100:     ## 통합대기환경 지수가 100 초과이면 (대기환경이 나쁘면), 공기청정기 켜라
        if g_Aircleaner == True:    ## 공기청정기가 켜져 있으면
            print("대기환경이 나쁩니다. 작동 중인 공기청정기 상태를 유지합니다:)")      ## 그대로 유지
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == True: print("작동\n")
        else:       ## 공기청정기가 꺼져 있으면
            g_Aircleaner = not g_Aircleaner     ## 켜라
        print("대기환경이 나쁩니다. 정지된 공기청정기를 작동합니다:)")
        print(">> 공기청정기 상태 : ", end="")
        if g_Aircleaner == True: print("작동\n")

    else:       ## 통합대기환경 지수가 100 이하이면 (대기환경이 나쁘지 않으면), 공기청정기 꺼라
        if g_Aircleaner == True:    ## 공기청정기가 켜져 있으면
            g_Aircleaner = not g_Aircleaner     ## 꺼라
            print("대기환경이 나쁘지 않습니다. 작동 중인 공기청정기를 정지합니다:)")
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == False: print("정지\n")
        else:       ## 공기청정기가 꺼져 있으면
            print("대기환경이 나쁘지 않습니다. 정지된 공기청정기 상태를 유지합니다:)")     ## 그대로 유지
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == False: print("정지\n")

################################### 창문 인공지능 모드
    rain_num = 0    ## rain_num > 0 : 비나 눈이 옴
    for window_status_wth in total_weather:
        if window_status_wth.get('category') == "PTY":      ## 항목(category)이 강수형태(PTY)이면
            rain_num += window_status_wth.get('fcstValue')     ## 강수 형태 (없음(0), 비(1), 비/눈(2), 눈(3))
            break

    atmosphere_num = 0    ## atmosphere_num > 100 : 나쁨
    for window_status_atm in total_atmosphere:
        atmosphere_num += int(window_status_atm.get('khaiValue'))      ## 통합대기환경지수
        break

    ######### 비가 오거나 난방기가 작동 중이거나 대기가 좋지 않으면, 창문을 닫아라
    if rain_num > 0 or g_Radiator == True or atmosphere_num > 100:
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            if rain_num > 0:    ## 비가 온다면
                g_Balcony_Windows = not g_Balcony_Windows   ## 창문을 닫아라
                print("비가 오고 있습니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and atmosphere_num > 100:  ## 비는 오지 않고, 대기환경이 나쁘다면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("대기환경이 좋지 않습니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and atmosphere_num <= 100 and g_Radiator == True:    ## 비는 오지 않고, 대기환경이 나쁘지 않고, 난방기가 작동 중이라면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("난방기가 작동 중입니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")

        else:  ## 창문이 닫혀 있으면
            if rain_num > 0:    ## 비가 온다면
                print("비가 오고 있습니다. 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and g_Radiator == True:    ## 비는 오지 않고 난방기가 작동 중이라면
                print("난방기가 작동 중입니다. 닫힌 창문 상태를 유지합니다:)")    ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and g_Radiator ==False and atmosphere_num > 100:   ## 비는 오지 않고, 난방기도 정지 중이고, 대기환경이 나쁘다면
                print("대기환경이 좋지 않습니다. 닫힌 창문 상태를 유지합니다:)")   ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")

    ######### 비도 오지 않고, 난방기도 정지 중이고, 대기도 나쁘지 않다면, 창문을 열어라
    elif rain_num == 0 and g_Radiator == False and atmosphere_num <= 100:
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            print("대기 환경이 나쁘지 않은 강수 없는 날입니다. 열린 창문 상태를 유지합니다:)")
            print(">> 발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == True: print("열림\n")
        elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
            g_Balcony_Windows = not g_Balcony_Windows
            print("대기 환경이 나쁘지 않은 강수 없는 날입니다. 닫힌 창문을 엽니다:)")
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

    ################## 환기 모드 작동
    if rain_num == 0 and atmosphere_num <= 100:     ## 비가 안 오고, 대기환경이 나쁘지 않은 조건에서
        if g_Ventilation_Mode == False:         ## 환기 모드가 꺼져 있을 경우
            print("\n===============================")
            print(">> 현재 환기 모드 : ", end="")
            if g_Ventilation_Mode == False: print("정지")
            print("===============================\n")
            Ventilation_Mode()

def Devices_AI():   ## 실시간 업데이트 정보 request -> JSon 파일 만들고 -> 장비 제어하는 함수
    get_Realtime_Weather_Info()
    print("\n<<가장 최신 대기환경정보 업데이트를 실시합니다!!>>\n".center(30))
    Make_Atmosphere_Json()
    total_weather = Read_Weather_Json()  ## 기상정보 JSon 파일을 불러오는 함수 - 인공지능 모드를 위해 JSon 파일의 정보를 읽어 오는
    total_atmosphere = Read_Atmosphere_Json()  ## 대기환경정보 JSon 파일을 불러오는 함수 - 인공지능 모드를 위해 JSon 파일의 정보를 읽어 오는

    if 30 < get_Realtime_Weather_Info() <= 59:  ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
                                                ## get_Realtime_Weather_Info() 하면 return -> day_min_int

        Control_Devices_AI(total_weather, total_atmosphere)   ## 장비 제어 함수

    elif 0 <= get_Realtime_Weather_Info() <= 30:  ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid

        Control_Devices_AI(total_weather, total_atmosphere)   ## 장비 제어 함수

def Smart_Mode():       ## 스마트 모드 메뉴 함수
    global g_AI_Mode, g_Ventilation_Mode
    print("<<스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 상태 변경\n3. 환기 모드 조회\n4. 환기 모드 상태 변경\n"
                         "5. 실시간 기상정보 Update\n6. 실시간 대기환경정보 Update\n-> "))

    if menu_num == 1:       ## 인공지능 모드 조회
        print("\n===============================")
        print(">> 현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        print("===============================\n")

    elif menu_num == 2:     ## 인공지능 모드 상태 변경
        if g_AI_Mode == False:      ## 인공지능 모드가 꺼져 있을 경우
            switch_num = int(input("\n<< 인공지능 모드가 꺼져 있습니다. 켜시겠습니까? >>\n1. ON\n2. OFF\n-> "))
            if switch_num == 1:
                print("\n===============================")
                print("인공지능 모드를 가동합니다:)\n")
                print(">> 변경 전 인공지능 모드 : ", end="")
                if g_AI_Mode == False: print("정지")
                g_AI_Mode = not g_AI_Mode
                print(">> 현재 인공지능 모드 : ", end="")
                if g_AI_Mode == True: print("작동")
                print("===============================\n")

                Devices_AI()

            elif switch_num == 2:
                print("\n======================================")
                print("인공지능 모드 정지 상태를 유지합니다:)")
                print("======================================\n")

        else:       ## 인공지능 모드가 켜져 있을 경우
            switch_num = int(input("\n<< 인공지능 모드가 켜져 있습니다. 끄시겠습니까? >>\n1. ON\n2. OFF\n-> "))
            if switch_num == 1:
                print("\n======================================")
                print("인공지능 모드 작동 상태를 유지합니다:)")
                print("======================================\n")
            elif switch_num == 2:
                print("\n===============================")
                print("인공지능 모드를 정지합니다:)\n")
                print(">> 변경 전 인공지능 모드 : ", end="")
                if g_AI_Mode == True: print("작동")
                g_AI_Mode = not g_AI_Mode
                print(">> 현재 인공지능 모드 : ", end="")
                if g_AI_Mode == False: print("정지")
                print("===============================\n")

    elif menu_num == 3:     ## 환기 모드 조회
        print("\n===========================")
        print(">> 현재 환기 모드 : ", end="")
        if g_Ventilation_Mode == True: print("작동")
        else: print("정지")
        print("===========================\n")

    elif menu_num == 4:     ## 환기 모드 상태 변경
        if g_Ventilation_Mode == False:     ## 환기 모드가 꺼져 있을 경우
            Ventilation_Mode()      ## 환기 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수

        else:  ## 환기 모드가 켜져 있을 경우
            switch_num = int(input("\n<< 환기 모드가 켜져 있습니다. 끄시겠습니까? >>\n1. ON\n2. OFF\n-> "))
            if switch_num == 1:
                print("\n======================================")
                print("환기 모드 작동 상태를 유지합니다:)")
                print("======================================\n")
            elif switch_num == 2:
                print("\n===============================")
                print("환기 모드를 정지합니다:)\n")
                print(">> 변경 전 환기 모드 : ", end="")
                if g_Ventilation_Mode == True: print("작동")
                g_Ventilation_Mode = not g_Ventilation_Mode
                print(">> 현재 환기 모드 : ", end="")
                if g_Ventilation_Mode == False: print("정지")
                print("===============================\n")

    elif menu_num == 5:
        get_Realtime_Weather_Info()

        ## 실시간 정보 업데이트를 하는데, 인공지능 모드가 ON인 경우, 실시간 정보 업데이트 한 것을 토대로, 상황 분석 -> 장비 제어
        if g_AI_Mode == True:
            total_weather = Read_Weather_Json()  ## 기상정보 JSon 파일을 불러오는 함수
            total_atmosphere = Read_Atmosphere_Json()   ## 대기환경통합정보 JSon 파일을 불러오는 함수

            Control_Devices_AI(total_weather, total_atmosphere)  ## 장비 제어 함수

    elif menu_num == 6:
        Make_Atmosphere_Json()

        ## 실시간 정보 업데이트를 하는데, 인공지능 모드가 ON인 경우, 실시간 정보 업데이트 한 것을 토대로, 상황 분석 -> 장비 제어
        if g_AI_Mode == True:
            total_weather = Read_Weather_Json()  ## 기상정보 JSon 파일을 불러오는 함수
            total_atmosphere = Read_Atmosphere_Json()  ## 대기환경정보 JSon 파일을 불러오는 함수

            Control_Devices_AI(total_weather, total_atmosphere)  ## 장비 제어 함수

    print("")