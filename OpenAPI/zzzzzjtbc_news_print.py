## [ver2] ver1을 그냥 sort(), reverse()만 써서 간략화 함

import json

data = []
with open("jtbcnews_facebook_2018-02-01_2018-02-02.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)
    data = data.get('data')

link_num_ls = []
for compa in data:
    set_ls = []
    set_ls.append(compa.get('created_time'))
    set_ls.append(compa.get('shares').get('count'))
    set_ls.append(compa.get('name'))
    set_ls.append(compa.get('link'))
    link_num_ls.append(set_ls)


link_num_ls.sort()          ## 리스트 안에 있는 것도 그냥 sort() 하면 정렬이 되는!!! 완전 신기!!
link_num_ls.reverse()       ## 대신 비교대상 형(int or str)이 동일 숫자가 되어야 함 (예, [[1, "aks"], [2, "alwl"])
                            ## [[1, "af"], ["afdq"], 23] 처럼 하면 안 됨! int(1)와 str("afdq")는 비교가 안 되니!!

for prn in link_num_ls:
    print("업데이트 시간 : %s" % prn[0])
    print("공유 수 : %s" % prn[1])
    print("기사 제목 : %s" % prn[2])
    print("링크 : %s\n" % prn[3])