import json


def Delete_Class(json_big_data, delete_class):
    for exist_del in json_big_data:
        dl_exist = exist_del.get('수강 정보').get('현재 수강 과목')
        for fnd in dl_exist:
            if fnd.get('강의 코드') == delete_class:
                for del_cl in json_big_data:
                    class_list = del_cl.get('수강 정보').get('현재 수강 과목')
                    del_index = -1
                    for find_del_cl in class_list:
                        del_index += 1
                        if find_del_cl.get('강의 코드') == delete_class:
                            del class_list[del_index]

                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("강의 코드 '%s' 과목이 삭제되었습니다!!\n" % delete_class)
                    return None

            else:
                print("일치하는 강의 코드가 없습니다. 강의 코드를 확인해 주세요!!\n")
                return None