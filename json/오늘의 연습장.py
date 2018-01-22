import json
import os

def Start_Student(path_number, json_big_data):
    while True:
        print("<<json 기반 주소록 관리 프로그램>>".center(30))
        start_number = int(input("===원하는 서비스의 번호를 입력해 주세요===\n1. 학생 정보 입력\n2. 학생 정보 조회\n"
                                 "3. 학생 정보 수정\n4. 학생 정보 삭제\n5. 프로그램 종료\n-> "))
        if start_number == 1:
            Create_Student(path_number, json_big_data)
        # elif start_number == 2:
        #     Select_Student(json_big_data)
        elif start_number == 5:
            print("이용해 주셔서 감사합니다. 프로그램을 종료합니다:)\n")
            break
        else:
            print("입력이 올바르지 않습니다. 다시 확인해 주세요!!\n")
            continue

def Create_Student(path_number, json_big_data):
    print("<<학생 정보 입력을 실행하겠습니다!! (돌아가기 : Enter)>>".center(50))
    student_info = {}
    student_info['이름'] = input("이름을 입력해 주세요(예, 홍길동) : ")
    if student_info['이름'] == "": return None
    student_info['나이'] = input("나이를 입력해 주세요(예, 29) : ")
    if student_info['나이'] == "": return None
    student_info['주소'] = input("주소를 입력해 주세요(예, 대구광역시 동구 아양로 135) : ")
    if student_info['주소'] == "": return None
    student_info['수강 정보'] = {}
    student_info.get('수강 정보')['과거 수강 횟수'] = input("과거 수강 횟수를 입력해 주세요(예, 2) : ")
    if student_info.get('수강 정보')['과거 수강 횟수'] == "": return None
    print("현재 수강 과목을 추가하시겠습니까? (y/n)")
    student_info.get('수강 정보')['현재 수강 과목'] = []
    while True:
        add_exit = input(" : ")
        if add_exit == 'Y' or add_exit == 'y':
            print("<<수강 과목을 추가하겠습니다!! (돌아가기 : Enter)>>".center(30))
            class_info = {}
            class_info['강의 코드'] = input("강의 코드를 입력해 주세요(예, PY171106) : ")
            if class_info['강의 코드'] == "": return None
            class_info['강의명'] = input("강의명을 입력해 주세요(예, 점프투 파이썬) : ")
            if class_info['강의명'] == "": return None
            class_info['강사명'] = input("강사명을 입력해 주세요(예, 이현구) : ")
            if class_info['강사명'] == "": return None
            class_info['개강일'] = input("개강일을 입력해 주세요(예, 2017-11-06) : ")
            if class_info['개강일'] == "": return None
            class_info['종료일'] = input("종료일을 입력해 주세요(예, 2018-09-05) : ")
            if class_info['종료일'] == "": return None
            student_info.get('수강 정보')['현재 수강 과목'].append(class_info)
            print("계속해서 수강 과목을 추가하시겠습니까? (y/n)")
        elif add_exit == 'N' or add_exit == 'n':
            break
        else:
            print("입력이 올바르지 않습니다. 다시 확인해 주세요!!")
            continue
    New_ID(path_number, json_big_data)
    student_info['student_ID'] = Read_ID()
    json_big_data.append(student_info)
    Make_Json(json_big_data)
    print("학생 정보 입력을 완료했습니다!!\n")

# def Select_Student(json_big_data):
#     print("<<학생 정보 조회를 실행하겠습니다!! (돌아가기 : Enter)>>".center(50))
#     select_num = int(input("===원하는 서비스의 번호를 입력해 주세요===\n1. 전체 학생 정보 조회\n2. 개별 학생 정보 조회\n-> "))
#     if select_num == 1:
#         Total_Student_Print(json_big_data)

def New_ID(path_number, json_big_data):     ## ID_index txt 만드는 함수
    if os.path.isfile("ID_index.txt"):      ## ID_index txt가 있을 경우
        with open("ID_index.txt", 'r') as last_id:
            last_id_num = last_id.readline()
            new_id_number = int(last_id_num[3:]) + 1
        with open("ID_index.txt", 'w') as new_id:
            new_id.write("ITT"+"{0:0>3}".format(str(new_id_number)))
    elif not os.path.isfile("ID_index.txt"):            ## ID_index txt가 없을 경우
        if path_number == 0 or path_number == 1:      ## json 파일이 있을 경우
            last_id_number = json_big_data[-1]          ## json 파일의 마지막에 있는 아이디 번호를 가져와서
            last_id_number = last_id_number.get('student_ID')
            last_id_number = last_id_number[3:]
            new_id_number = int(last_id_number) + 1         ## +1 한 뒤,
            with open("ID_index.txt", 'w') as new_id:
                new_id.write("ITT"+"{0:0>3}".format(str(new_id_number)))    ## ID 부여
        elif path_number == 2:    ## json 파일이 없을 경우(json 파일 새로 생성)
            with open("ID_index.txt", 'w') as new_id:
                new_id.write("ITT"+"001")       ## 첫 ID 부여

def Read_ID():      ## ID_index txt을 읽어 고유 ID를 부여하는 함수
    with open("ID_index.txt", 'r') as new_id:
        grant_id = new_id.readline()
        return grant_id

def Make_Json(json_big_data):       ## json 파일 생성하는 함수
    with open("ITT_Student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

# def Total_Student_Print(json_big_data):



json_big_data = []
if os.path.isfile("ITT_Student.json"):
    path_number = 0
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        Start_Student(path_number, json_big_data)
elif not os.path.isfile("ITT_Student.json"):
    path_number = int(input("<<파일이 존재하지 않습니다.>>\n1. 경로 선택\n2. 신규 생성\n-> "))
    if path_number == 1:
        path_json = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.json" % path_json, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            Start_Student(path_number, json_big_data)
    elif path_number == 2:
        Start_Student(path_number, json_big_data)
    else:
        print("입력이 올바르지 않습니다. 다시 확인해 주세요!!\n")