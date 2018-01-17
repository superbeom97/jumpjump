import json
import os

json_big_data = []

def Start_Student():
    while True:
        student_data_values = {}
        total_course_info = {}
        now_course_info = []

        print("<<json기반 주소록 관리 프로그램>>".center(33))  ## .center(30) 하면 총 글자 수 30칸에서 가운데 정렬
        select_number = int(input("===원하는 서비스의 번호를 눌러주세요~ 찡긋;)===\n1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정"
                                  "\n4. 학생 정보삭제\n5. 프로그램 종료\n-> "))
        if select_number == 1:
            print("<<학생 정보 입력을 진행하겠습니다.>>".center(30))
            student_name = input("이름을 입력해 주세요 : ")
            student_data_values["이름"] = student_name
            student_age = int(input("나이를 입력해 주세요 : "))
            student_data_values["나이"] = student_age
            student_address = input("주소를 입력해 주세요 : ")
            student_data_values["주소"] = student_address
            Class_Code(student_name, student_data_values, json_big_data)  ## 강의 코드 - 강의명 - 강사 이름 - 개강일 - 종료일.. 입력 함수

        elif select_number == 2:
            print("<<학생 정보를 조회하겠습니다.>>".center(30))
            search_student = input("조회를 원하는 학생의 정보를 입력해 주세요 : ")
            for search in json_big_data:
                search_name = search.get('이름')
                course_name = search.get('강의명')
                instructor_name = search.get('강사 이름')
                if search_student == search_name or course_name or instructor_name:
                    print(search)
                    break


        elif select_number == 5:
            print("이용해 주셔서 감사합니다! 또 놀러 오세요~")
            break


def Class_Code(student_name, student_data_values, json_big_data, course_info, now_course_info):           ## 강의 코드 입력 함수
    while True:
        student_past_class = int(input("과거 수강 횟수를 입력해 주세요 : "))
        course_info["과거 수강 횟수"] = student_past_class
        class_code = input("현재 수강 중인 과목 코드를 입력해 주세요 : ")




        print("현재 수강 중인 과목 코드를 입력해 주세요:)\n입력을 모두 다 하셨으면 '종료'를 입력해 주세요!!")
        class_code_input = input(" : ")
        if class_code_input != '종료':
            student_data_values.get("강의 코드").append(class_code_input)
        elif class_code_input == '종료':
            if os.path.isfile("Student_ID_info.txt"):
                with open('Student_ID_info.txt', 'r') as numbering:
                    id_number = numbering.readline()
                    split_numbering = id_number[3:]
                    int_split_numbering = int(split_numbering)
                    int_split_numbering += 1
                with open('Student_ID_info.txt', 'w') as student_id_info:
                    student_id_info.write("ITT"+"{0:0>3}".format(str(int_split_numbering)))
                                                                ## p.65 글자수 3, 오른쪽 정렬, 나머지 0으로
                with open('Student_ID_info.txt', 'r') as student_id_info:
                    student_id = student_id_info.readline()
                    student_data_values[student_id] = student_name
                    json_big_data.append(student_data_values)

                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ITT_Student.json SAVED")

            elif not os.path.isfile("Student_ID_info.txt"):
                with open('Student_ID_info.txt', 'w') as student_id_info:
                    student_id_info.write("ITT"+"001")
                with open('Student_ID_info.txt', 'r') as student_id_info:
                    student_id = student_id_info.readline()
                    student_data_values[student_id] = student_name
                    json_big_data.append(student_data_values)
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ITT_Student.json SAVED")
            break



if os.path.isfile("ITT_Student.json"):      ## 프로그램 시작 시 소스코드가 있는 경로에 'ITT_Student.json' 파일을 읽어 들인다
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        Start_Student()
elif not os.path.isfile("ITT_Student.json"):        ## 파일이 없을 시
    path_number = int(input("파일이 존재하지 않습니다.\n경로를 선택하려면 1번, 신규 생성하려면 2번을 눌러주세요\n-> "))
    if path_number == 1:
        path_path = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.json" % path_path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            Start_Student()
    elif path_number == 2:
        Start_Student()