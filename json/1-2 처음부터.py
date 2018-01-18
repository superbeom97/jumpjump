import json
import os


def Start_Student(json_big_data):
    while True:
        student_data = {}
        total_course_info = {}
        now_course_info_list = []
        now_course_info_dict = {}

        student_name_count = 0
        instructor_name_count = 0
        class_name_count = 0
        print("<<학생 정보를 조회하겠습니다.>>".center(30))
        select_number = int(input("1. 전체 학생 정보 조회\n2. 개별 학생 정보 조회\n : "))
        if select_number == 1:
            Select_Total_Student(json_big_data)

        elif select_number == 2:
            Select_Personal_Student(json_big_data)


def Select_Total_Student(json_big_data):        ## 전체 학생 정보 조회_ 출력 전 함수
    for ttal in json_big_data:
        select_total_student = {}
        select_total_student_info_list = []
        select_total_student['student_ID'] = ttal.get('student_ID')
        select_total_student['이름'] = ttal.get('이름')
        select_total_student['나이'] = ttal.get('나이')
        select_total_student['주소'] = ttal.get('주소')
        select_total_student['수강 정보'] = ttal.get('수강 정보')
        select_total_student['과거 수강 횟수'] = ttal.get('수강 정보').get('과거 수강 횟수')
        for ttal_low in select_total_student.get('수강 정보').get('현재 수강 과목'):
            select_total_student_info = {}
            select_total_student_info['강의 코드'] = ttal_low.get('강의 코드')
            select_total_student_info['강의명'] = ttal_low.get('강의명')
            select_total_student_info['강사 이름'] = ttal_low.get('강사 이름')
            select_total_student_info['개강일'] = ttal_low.get('개강일')
            select_total_student_info['종료일'] = ttal_low.get('종료일')
            select_total_student_info_list.append(select_total_student_info)
        Select_Total_Student_Print(select_total_student, select_total_student_info_list)

def Select_Personal_Student(json_big_data):
    print("<<조회 조건을 선택해 주세요>>".center(30))
    search_condition_number = int(input("1. ID\n2. 이름\n3. 나이\n4. 주소\n5. 과거 수강 횟수\n"
                                        "6. 강의 코드\n7. 강의명\n8. 강사 이름\n9. 개강일\n10. 종료일\n : "))
    if search_condition_number == 1:
        search_condition_id = input("정보 조회를 원하는 학생의 ID를 입력해 주세요 : ")
        key_name = 'student_ID'
        search_id = []
        for search_info in json_big_data:  ## ID 조회
            search_id.append(search_info.get(key_name))
        Select_Personal_Student_Print(search_id, search_condition_id, json_big_data)

    elif search_condition_number == 2:
        search_condition_id = input("정보 조회를 원하는 학생의 이름을 입력해 주세요 : ")
        search_id = []
        for search_info in json_big_data:  ## 이름 조회
            search_id.append(search_info.get('이름'))
        Select_Personal_Student_Print(search_id, search_condition_id, json_big_data)

def Select_Personal_Student_Print(search_id, search_condition_id, json_big_data):
    id_count = 0
    for confirm in search_id:
        if search_condition_id in confirm:
            id_count += 1
    if id_count == 1:
        Select_Total_Student(json_big_data)
    elif id_count > 1:
        mul_count = 0
        for confirm in search_id:
            if search_condition_id in confirm:
                mul_count += 1
                Select_Id_Print(search_condition_id, confirm, mul_count)
        print("'%s'가 포함된 학생은 총 %s명입니다." % (search_condition_id, mul_count))

def Select_Id_Print(search_condition_id, confirm, mul_count):
    print("'%s'가 포함된 학생의 ID : %s" % (search_condition_id, confirm))


def Select_Total_Student_Print(select_total_student, select_total_student_info_list):       ## 전체 학생 정보 조회_ 출력 함수
    print("<<ID가 '%s'인 '%s' 학생의 정보는 다음과 같습니다>>".center(30) % (select_total_student.get('student_ID'), select_total_student.get('이름')))
    print("ID : %s" % select_total_student.get('student_ID'))
    print("이름 : %s" % select_total_student.get('이름'))
    print("나이 : %s" % select_total_student.get('나이'))
    print("주소 : %s" % select_total_student.get('주소'))
    print("")  ## 한 줄 띄어쓰기 위해
    print("과거 수강 횟수 : %s \n" % select_total_student.get('수강 정보').get('과거 수강 횟수'))
    print("현재 수강 과목은 다음과 같습니다.")
    for now_course_info in select_total_student_info_list:
        print("강사 이름 : %s" % now_course_info.get('강사 이름'))
        print("강의 코드 : %s" % now_course_info.get('강의 코드'))
        print("강의명 : %s" % now_course_info.get('강의명'))
        print("개강일 : %s" % now_course_info.get('개강일'))
        print("종료일 : %s \n" % now_course_info.get('종료일'))
    print("")




#
#
# def Student_Info_Print(search_student, json_big_data, search_info, now_course_info):        ## 학생 정보 조회 출력 함수 1-2
#     print("ID : %s" % search_info.get('student_ID'))
#     print("이름 : %s" % search_info.get('이름'))
#     print("나이 : %s" % search_info.get('나이'))
#     print("주소 : %s" % search_info.get('주소'))
#     print("")       ## 한 줄 띄어쓰기 위해
#     print("과거 수강 횟수 : %s" % search_info.get('수강 정보').get('과거 수강 횟수'))
#     print("")       ## 한 줄 띄어쓰기 위해
#     print("현재 수강 과목은 다음과 같습니다.")
#     for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
#         print("강사 이름 : %s" % now_course_info.get('강사 이름'))
#         print("강의 코드 : %s" % now_course_info.get('강의 코드'))
#         print("강의명 : %s" % now_course_info.get('강의명'))
#         print("개강일 : %s" % now_course_info.get('개강일'))
#         print("종료일 : %s" % now_course_info.get('종료일'))
#         print("")       ## 한 줄 띄어쓰기 위해


json_big_data = []
if os.path.isfile("ITT_Student.json"):      ## 프로그램 시작 시 소스코드가 있는 경로에 'ITT_Student.json' 파일을 읽어 들인다
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        Start_Student(json_big_data)
elif not os.path.isfile("ITT_Student.json"):        ## 파일이 없을 시
    path_number = int(input("파일이 존재하지 않습니다.\n경로를 선택하려면 1번, 신규 생성하려면 2번을 눌러주세요\n-> "))
    if path_number == 1:
        path_path = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.json" % path_path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            Start_Student(json_big_data)
    elif path_number == 2:
        Start_Student(json_big_data)