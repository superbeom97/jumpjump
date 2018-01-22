## 72line
if~~~:
    with open('Student_ID_info.txt', 'w') as student_id_info:  ## 파일에 있는 아이디 고유번호 +1 증가된 것을 부여하므로, 001부터 부여하도록!
        student_id_info.write("ITT" + "001")
    with open('Student_ID_info.txt', 'r') as student_id_info:
        student_id = student_id_info.readline()
        create_student['student_ID'] = student_id
        json_big_data.append(create_student)


## 83line
else:
    with open('Student_ID_info.txt', 'r') as numbering:
        id_number = numbering.readline()
        split_numbering = id_number[3:]
        int_split_numbering = int(split_numbering)
        int_split_numbering += 1
    with open('Student_ID_info.txt', 'w') as student_id_info:
        student_id_info.write("ITT" + "{0:0>3}".format(str(int_split_numbering)))
        ## p.65 글자수 3, 오른쪽 정렬, 나머지 0으로
    with open('Student_ID_info.txt', 'r') as student_id_info:
        student_id = student_id_info.readline()
        create_student['student_ID'] = student_id
        json_big_data.append(create_student)


## 109line
with open('Student_ID_info.txt', 'w') as student_id_info:
    student_id_info.write("ITT" + "{0:0>3}".format(str(last_id_number)))
with open('Student_ID_info.txt', 'r') as student_id_info:
    student_id = student_id_info.readline()
    create_student['student_ID'] = student_id
    json_big_data.append(create_student)

## 120line
with open('Student_ID_info.txt', 'w') as student_id_info:
    student_id_info.write("ITT" + "001")
with open('Student_ID_info.txt', 'r') as student_id_info:
    student_id = student_id_info.readline()
    create_student['student_ID'] = student_id
    json_big_data.append(create_student)