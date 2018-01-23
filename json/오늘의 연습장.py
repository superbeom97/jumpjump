import json
import os

def Start_Student(json_big_data):
    try:
        while True:
            print("<<json 기반 주소록 관리 프로그램>>".center(30))
            start_number = int(input("===원하는 서비스의 번호를 입력해 주세요===\n1. 학생 정보 입력\n2. 학생 정보 조회\n"
                                     "3. 학생 정보 수정\n4. 학생 정보 삭제\n5. 프로그램 종료\n-> "))
            if start_number == 1:
                Create_Student(json_big_data)
            elif start_number == 2:
                Select_Student(json_big_data)
            # elif start_number == 3:
            #     Update_Student(json_big_data)
            # elif start_number == 4:
            #     Delete_Student(json_big_data)
            elif start_number == 5:
                print("이용해 주셔서 감사합니다!! 찡긋;)")
                break
            else:
                print("입력이 올바르지 않습니다. 다시 확인해 주세요!!\n")
    except:
        print("입력이 올바르지 않습니다. 다시 확인해 주세요!!\n")
        Start_Student(json_big_data)

def Create_Student(json_big_data):
    print("<<학생 정보 입력을 진행하겠습니다!! (돌아가기 : Enter)>>".center(50))
    total_student_info = {}  ## depth 1
    total_student_info['이름'] = input("이름을 입력해 주세요(예, 홍길동) : ")
    if total_student_info['이름'] == "": return None
    total_student_info['나이'] = input("나이를 입력해 주세요 : ")
    if total_student_info['나이'] == "": return None
    total_student_info['주소'] = input("주소를 입력해 주세요 : ")
    if total_student_info['주소'] == "": return None
    total_student_info['수강 정보'] = course_info = {}  ## depth 2
    course_info['과거 수강 횟수'] = input("과거 수강 횟수를 입력해 주세요 : ")
    if course_info['과거 수강 횟수'] == "": return None
    course_info['현재 수강 과목'] = course_info_list = []
    print("현재 수강 과목을 추가하시겠습니까? (y/n)")
    while True:
        add_cancel = input(" : ")
        if add_cancel == 'Y' or add_cancel == 'y':
            Create_Course(json_big_data, total_student_info, course_info, course_info_list)
        elif add_cancel == 'N' or add_cancel == 'n':
            if os.path.isfile('ID_index.txt'):  ## 1. ID_index txt가 있을 경우
                if len(json_big_data) > 0:      ## 1-1 이미 작성한 json 파일이 있을 경우 -> ID를 가져와 +1 시킨 후 ID 부여
                    with open('ID_index.txt', 'r') as last_id_index:
                        last_id = last_id_index.readline()
                        last_id_num = last_id[3:]
                        new_id_num = int(last_id_num) + 1
                    with open('ID_index.txt', 'w') as new_id_index:
                        new_id_index.write("ITT"+"{0:0>3}".format(str(new_id_num)))
                else:        ## 1-2 json 파일을 새로 생성하는 경우 -> ITT 001부터 부여
                    with open('ID_index.txt', 'w') as new_id_index:
                        new_id_index.write("ITT001")
            elif not os.path.isfile('ID_index.txt'):    ## 2. ID_index txt가 없을 경우
                if os.path.isfile('ITT_Student.json'):  ## 2-1 이미 작성한 json 파일이 있을 경우
                    last_id = json_big_data[-1]
                    last_id_num = last_id.get('student_ID')[3:]
                    new_id_num = int(last_id_num) + 1
                    with open('ID_index.txt', 'w') as new_id_index:
                        new_id_index.write("ITT"+"{0:0>3}".format(str(new_id_num)))
                elif not os.path.isfile('ITT_Student.json'):    ## 2-2 json 파일을 새로 생성하는 경우(json 파일도 없을 경우)
                    with open('ID_index.txt', 'w') as new_id_index:
                        new_id_index.write("ITT001")
            Read_Json(total_student_info, json_big_data)
            Make_Json(json_big_data)
            print("학생 정보 입력이 완료되었습니다!!\n")
            break
        else:
            print("입력이 올바르지 않습니다. y 또는 n을 입력해 주세요!!")
            continue

def Create_Course(json_big_data, total_student_info, course_info, course_info_list):
    personal_course_info = {}   ## depth 3
    personal_course_info['강의 코드'] = input("강의 코드를 입력해 주세요 : ")
    personal_course_info['강의명'] = input("강의명을 입력해 주세요 : ")
    personal_course_info['강사명'] = input("강사명을 입력해 주세요 : ")
    personal_course_info['개강일'] = input("개강일을 입력해 주세요 : ")
    personal_course_info['종료일'] = input("종료일을 입력해 주세요 : ")
    course_info_list.append(personal_course_info)
    print("계속해서 수강 과목을 추가하시겠습니까? (y/n)")

def Select_Student(json_big_data):
    print("<<학생 정보 조회를 진행하겠습니다.>>".center(30))
    select_number = int(input("===원하는 서비스의 번호를 입력해 주세요===\n"
                              "1. 전체 학생 조회\n2. 개별 학생 조회\n0. 돌아가기\n-> "))
    if select_number == 1:      ## 전체 학생 조회
        Total_Student(json_big_data)
    elif select_number == 2:
        print("<<개별 학생 정보 조회를 진행하겠습니다.>>").center(30)
        person_select_number = int(input("===원하는 서비스의 번호를 입력해 주세요===\n"
                              "1. ID\n2. 이름\n3. 나이\n4. 주소\n"
                              "5. 과거 수강 횟수\n6. 강의 코드\n7. 강의명\n8. 강사명\n0. 돌아가기"))
        if person_select_number == 1:
            person_select_number == 'student_ID'
            print("<<ID를 통한 개별 학생 조회를 진행하겠습니다.>>".center(50))
            key_name = input("조회를 원하시는 ID를 입력해 주세요(예, ITT003) : ")
            Persoanl_Student(key_name, json_big_data)
    elif select_number == 0:
        return None
    else:
        print("입력이 올바르지 않습니다. 다시 입력해 주세요!!\n")

def Total_Student(json_big_data):
    print("<<전체 학생 정보 조회를 진행하겠습니다.>>")
    for tot_student in json_big_data:
        Personal_Student_Print(tot_student)

def Persoanl_Student(key_name, json_big_data):
    find_index = []
    find_idx = -1
    for z in json_big_data:
        find_idx += 1
        if z.get('student_ID') == key_name:
            find_index.append(find_idx)
    if find_index == 1:
        tot_student = json_big_data[find_idx]
        Personal_Student_Print(tot_student)
    # elif find_index > 1:
    #     Mul_Print(key_name, find_index, json_big_data)

# def Mul_Print(key_name, find_index, json_big_data):
    # print("'%s'이/가 포함된 '%s'는 %s명 입니다." % (key_name, person))

def Personal_Student_Print(tot_student):
    print("ID : %s" % tot_student.get('student_ID'))
    print("이름 : %s" % tot_student.get('이름'))
    print("나이 : %s" % tot_student.get('나이'))
    print("주소 : %s" % tot_student.get('주소'))
    print("수강 정보")
    print("  >> 과거 수강 횟수 : %s" % tot_student.get('수강 정보').get('과거 수강 횟수'))
    if len(tot_student.get('수강 정보').get('현재 수강 과목')) > 0:
        for course_info in tot_student.get('수강 정보').get('현재 수강 과목'):
            print("  >> 현재 수강 과목")
            print("    + 강의 코드 : %s" % course_info.get('강의 코드'))
            print("    + 강의명 : %s" % course_info.get('강의명'))
            print("    + 강사명 : %s" % course_info.get('강사명'))
            print("    + 개강일 : %s" % course_info.get('개강일'))
            print("    + 종료일 : %s" % course_info.get('종료일'))
    print("")

def Read_Json(total_student_info, json_big_data):       ## ID_info txt에서 ID를 읽어, ID를 부여하는 함수
    with open('ID_index.txt', 'r') as student_id_info:
        student_id = student_id_info.readline()
        total_student_info['student_ID'] = student_id
        json_big_data.append(total_student_info)

def Make_Json(json_big_data):       ## json 파일 생성하는 함수
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

## 출바알~
json_big_data =[]
if os.path.isfile("ITT_Student.json"):
    path_number = 0
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
    Start_Student(json_big_data)

elif not os.path.isfile("ITT_Student.json"):
    path_number = int(input("<<파일이 없습니다>>\n1. 경로 설정\n2. 신규 생성\n-> "))
    if path_number == 1:
        path_path = input("경로를 입력해 주세요 : ")
        with open('%s\\ITT_Student.json', encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
        Start_Student(json_big_data)
    elif path_number == 2:
        Start_Student(json_big_data)

    else:
        print("입력일 올바르지 않습니다. 다시 확인해 주세요!!\n")