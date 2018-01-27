from pprint import pprint  ## print할 때 사용하면, 그 형식 그대로 보여줌 (예, json 파일)

################################## 1. 리스트 내에서 서로 비교할 때 사용!! ##################################
## if change_num_index == len(change_num_ls) - 1:      # step_by가 리스트 change_num_ls의 마지막 자릿 수인지 확인
## for next_step_by in change_num_ls[(change_num_index+1):]:
#    ↳ step_by 다음 인덱스들을 가져오는 코드
#    ↳ step_by(리스트 change_num_ls의 하나)를 리스트 change_num_ls의 나머지들과 비교하기 위해

## 예 1
change_num_ls = []
change_num_index = -1
mul_count_ls = []
for step_by in change_num_ls:
    mul_count = 1
    change_num_index += 1
    if len(step_by) == 8:
        if change_num_index == len(change_num_ls) - 1:      ## step_by가 리스트 change_num_ls의 마지막 자릿 수인지 확인
            mul_count_ls.append("%s     No duplicates" % step_by)
            break   ## step_by가 리스트 change_num_ls의 마지막 자릿 수 일 때는 비교 대상이 없으니, 종료해라
        del_index = 0
        for next_step_by in change_num_ls[(change_num_index+1):]:      ## step_by 다음 인덱스들을 가져오는 코드 ↴
            del_index += 1      ## step_by(리스트 change_num_ls의 하나)를 리스트 change_num_ls의 나머지들과 비교하기 위해
            if step_by == next_step_by:
                mul_count += 1
                change_num_ls[del_index] = next_step_by + "%s" % del_index

## 예 2
def Only_One(sort_news):
    index_count = -1
    for compa in sort_news:
        index_count += 1
        if index_count == len(sort_news) - 1:
            break
        for next_compa in sort_news[(index_count):]:
            if compa[1] == next_compa[1]:
                del sort_news[(index_count+1)]


################################## 2. 리스트 내의 리스트 정렬!! ##################################
################## [ver0] _ver1과 ver2 쓴 다음, 더 좋은 방법을 찾아서 정리
## 리스트 내에서 int가 첫 번째가 아닌 다른 자리에 있어도, 정렬하는 법 적용

score = [("개", 50), ("기린", 100), ("고양이", 30)]
score.sort(key=lambda x: x[1])
print(score)
##>> [("고양이", 30), ("개", 50), ("기린", 100)]

############################### [ver1]
import os
import json

def Jtbc_News(data):
    link_num_ls = []
    for compa in data:
        set_ls = []
        set_ls.append(compa.get('shares').get('count'))
        set_ls.append(compa.get('name'))
        set_ls.append(compa.get('link'))
        link_num_ls.append(set_ls)

    Comparison_Link(link_num_ls)

def Comparison_Link(link_num_ls):
    link_ls = []
    for compa in link_num_ls:
        link_ls.append(compa[0])
    link_ls.sort()
    link_ls.reverse()

    Sort_Fuction(link_num_ls, link_ls)

def Sort_Fuction(link_num_ls, link_ls):
    sort_news = []
    for search_news in link_ls:
        for news in link_num_ls:
            if search_news == news[0]:
                sort_news.append(news)

    Only_One(sort_news)

def Only_One(sort_news):
    index_count = -1
    for compa in sort_news:
        index_count += 1
        if index_count == len(sort_news) - 1:
            break
        for next_compa in sort_news[(index_count):]:
            if compa[1] == next_compa[1]:
                del sort_news[(index_count+1)]

    for prn in sort_news:
        print("공유 수 : %s" % prn[0])
        print("기사 제목 : %s" % prn[1])
        print("링크 : %s\n" % prn[2])


## Entry Point!!
data = []
with open("jtbcnews_facebook_2018-01-24_2018-01-25.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)
    data = data.get('data')
    Jtbc_News(data)

######################## [ver2] ver1을 그냥 sort(), reverse()만 써서 간략화 함
data = []
with open("jtbcnews_facebook_2018-01-24_2018-01-25.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)
    data = data.get('data')

link_num_ls = []
for compa in data:
    set_ls = []
    set_ls.append(compa.get('shares').get('count'))
    set_ls.append(compa.get('name'))
    set_ls.append(compa.get('link'))
    link_num_ls.append(set_ls)


link_num_ls.sort()          ## 리스트 안에 있는 것도 그냥 sort() 하면 정렬이 되는!!! 완전 신기!!
link_num_ls.reverse()       ## 대신 비교대상 형(int or str)이 동일 숫자가 되어야 함 (예, [[1, "aks"], [2, "alwl"])
                            ## [[1, "af"], ["afdq"], 23] 처럼 하면 안 됨! int(1)와 str("afdq")는 비교가 안 되니!!

for prn in link_num_ls:
    print("공유 수 : %s" % prn[0])
    print("기사 제목 : %s" % prn[1])
    print("링크 : %s\n" % prn[2])