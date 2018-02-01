############################### 장비 상태 확인 / 장비 제어하는 모듈

from Base_Start_HomeNetwork import Variable_Declaration

Variable_Declaration()

# g_Radiator = False              ## 난방기
# g_Airconditioner = False        ## 에어컨
# g_Aircleaner = False            ## 공기청정기
# g_Humidifier = False            ## 가습기
# g_Dehumidifier = False          ## 제습기
# g_Gas_Valve = False             ## 가스밸브
# g_Balcony_Windows = False       ## 발코니(베란다) 창문
# g_Door = False                  ## 출입문
# g_AI_Mode = False               ## 인공지능 모드
# g_Ventilation_Mode = False      ## 환기 모드


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
    Print_Device_fir_Status('공기청정기', g_Aircleaner)
    Print_Device_fir_Status('가습기', g_Humidifier)
    Print_Device_fir_Status('제습기', g_Dehumidifier)
    Print_Device_snd_Status('가스밸브', g_Gas_Valve)
    Print_Device_snd_Status('발코니(베란다) 창문', g_Balcony_Windows)
    Print_Device_snd_Status('출입문', g_Door)
    print("===================================")
    print("")

def Control_Device():       ## 장비 제어 함수
    ## 전역 변수를 비교나 어사인 하려면 함수 안에서 global을 설정해 줘야 해!!
    global  g_Radiator, g_Airconditioner, g_Aircleaner, g_Humidifier, g_Dehumidifier, g_Gas_Valve, g_Balcony_Windows, g_Door

    Check_Device_Status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 에어컨\n3. 공기청정기\n4. 가습기\n5. 제습기\n"
                         "6. 가스밸브\n7. 발코니(베란다)창\n8. 출입문\n-> "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
    elif menu_num == 2:
        g_Airconditioner = not g_Airconditioner
    elif menu_num == 3:
        g_Aircleaner = not g_Aircleaner
    elif menu_num == 4:
        g_Humidifier = not g_Humidifier
    elif menu_num == 5:
        g_Dehumidifier = not g_Dehumidifier
    elif menu_num == 6:
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 7:
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 8:
        g_Door = not g_Door
    print("")

    Check_Device_Status()