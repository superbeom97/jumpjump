from pprint import pprint  ## print할 때 사용하면, 그 형식 그대로 보여줌 (예, JSon 파일)

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


################################## 2. 딕셔너리 정렬!! ##################################
import operator

print("--------------------------------------------------------------")
print("<<simple dictionary sorting>>".center(50))
dic_fir = {'라희':80, '가수':90, '다영':60}
print(dic_fir)
## >> {'라희': 80, '가수': 90, '다영': 60}

print('<<딕셔너리 - VALUE로 정렬>>'.center(44))
dic_snd = sorted(dic_fir.items(), key=operator.itemgetter(1))   ## 딕셔너리 dic_fir의 value로 정렬해라
print(dic_snd)
## >> [('다영', 60), ('라희', 80), ('가수', 90)]

dic_thrd = sorted(dic_fir.items(), key=operator.itemgetter(1), reverse=True) ## 딕셔너리 dic_fir의 value로 내림차순 정렬해라
print(dic_thrd)
## >> [('가수', 90), ('라희', 80), ('다영', 60)]

print("<<딕셔너리 - KEY로 정렬>>".center(42))
dic_snd = sorted(dic_fir.items(), key=operator.itemgetter(0))   ## 딕셔너리 dic_fir의 key로 정렬해라
print(dic_snd)
## >> [('가수', 90), ('다영', 60), ('라희', 80)]

dic_thrd = sorted(dic_fir.items(), key=operator.itemgetter(0), reverse=True) ## 딕셔너리 dic_fir의 key로 내림차순 정렬해라
print(dic_thrd)
## >> [('라희', 80), ('다영', 60), ('가수', 90)]

print("--------------------------------------------------------------")
print("<<tuple 배열로 이뤄진 딕셔너리를 정렬하기>>".center(50))
data = {}
data['라희'] = (80, 95, 90)
data['가수'] = (90, 80, 70)
data['다영'] = (70, 100, 90)
print(data)
## >> {'라희': (80, 95, 90), '가수': (90, 80, 70), '다영': (70, 100, 90)}

##### sorted(data.items(), key=lambda x: x[1][0], reverse=False)
##### sort(1, 2, 3) -> 첫 번째 iteratable 파라미터가 하니식 2번째 수식에 대입되어 돌아 간다.
print('<<tuple의 첫 번째 항목으로 정렬>>'.center(50))
data_snd = sorted(data.items(), key=lambda x: x[1][0], reverse=False)   ## x[1][0] : 딕셔너리에서 [1] 즉, value 값 중 [0] 첫 번째 인덱스!! 를 기준으로 정렬
## data_snd = sorted(data.items(), key=lambda x: x[1][1], reverse=False)   ## x[1][1] : 딕셔너리에서 [1] 즉, value 값 중 [1] 즉, 두 번째 인덱스!! 를 기준으로 정렬
## data_snd = sorted(data.items(), key=lambda x: x[0][0], reverse=False)   ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_snd)
## >> [('다영', (70, 100, 90)), ('라희', (80, 95, 90)), ('가수', (90, 80, 70))]

print('<<tuple의 두 번째 항목으로 정렬>>'.center(50))
data_thrd = sorted(data.items(), key=lambda x: x[1][1], reverse=False)
print(data_thrd)
## >> [('가수', (90, 80, 70)), ('라희', (80, 95, 90)), ('다영', (70, 100, 90))]

print('<<tuple의 세 번째 항목으로 정렬>>'.center(50))
data_four = sorted(data.items(), key=lambda x: x[1][2], reverse=False)
print(data_four)
## >> [('가수', (90, 80, 70)), ('라희', (80, 95, 90)), ('다영', (70, 100, 90))]

print("--------------------------------------------------------------")
print("<<dictionary 배열로 이뤄진 딕셔너리를 정렬하기>>".center(50))
data['라희'] = {'국어':80, '수학':95, '영어':80}
data['가수'] = {'국어':90, '수학':80, '영어':70}
data['다영'] = {'국어':70, '수학':100, '영어':90}
print(data)
## >> {'라희': {'국어': 80, '수학': 95, '영어': 80}, '가수': {'국어': 90, '수학': 80, '영어': 70}, '다영': {'국어': 70, '수학': 100, '영어': 90}}

print('<<국어 성적으로 정렬>>'.center(44))
data_snd = sorted(data.items(), key=lambda x: x[1]['국어'], reverse=False)    ## x[1]['국어'] : 딕셔너리에서 [1] 즉, value 값 중 '국어'의 value를 기준으로 정렬
print(data_snd)
## >> [('다영', {'국어': 70, '수학': 100, '영어': 90}), ('라희', {'국어': 80, '수학': 95, '영어': 80}), ('가수', {'국어': 90, '수학': 80, '영어': 70})]

print('<<영어 성적으로 정렬>>'.center(44))
data_thrd = sorted(data.items(), key=lambda x: x[1]['영어'], reverse=False)   ## x[1]['영어'] : 딕셔너리에서 [1] 즉, value 값 중 '영어'의 value를 기준으로 정렬
print(data_thrd)
## >> [('가수', {'국어': 90, '수학': 80, '영어': 70}), ('라희', {'국어': 80, '수학': 95, '영어': 80}), ('다영', {'국어': 70, '수학': 100, '영어': 90})]

print('<<이름 순으로 정렬>>'.center(44))
data_thrd.sort(key=lambda x: x[0][0], reverse=False)  ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_thrd)        ## 리스트를 정렬할 경우 -> 바로 .sort를 사용하여
## >> [('가수', {'국어': 90, '수학': 80, '영어': 70}), ('다영', {'국어': 70, '수학': 100, '영어': 90}), ('라희', {'국어': 80, '수학': 95, '영어': 80})]

data_four = sorted(data.items(), key=lambda x: x[0][0], reverse=False)  ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_four)        ## 리스트가 아닌 것을 정렬할 경우 -> sorted를 사용하여
## >> [('가수', {'국어': 90, '수학': 80, '영어': 70}), ('다영', {'국어': 70, '수학': 100, '영어': 90}), ('라희', {'국어': 80, '수학': 95, '영어': 80})]


################################## 3. 리스트 내의 리스트 정렬!! ##################################
################## [ver0] _ver1과 ver2 쓴 다음, 더 좋은 방법을 찾아서 정리
## 리스트 내에서 int가 첫 번째가 아닌 다른 자리에 있어도, 정렬하는 법 적용

score = [("개", 50), ("기린", 100), ("고양이", 30)]
score.sort(key=lambda x: x[1])
print(score)
##>> [("고양이", 30), ("개", 50), ("기린", 100)]

mul_count_ls = [['123-4567', 2], ['987-6542', 'No duplicates'], ['456-8792', 'No duplicates'], ['321-5487', 'No duplicates']]
mul_count_ls.sort(key=lambda x: x[0])   ## 리스트 내에서 첫 번째 인덱스로 정렬해라
print(mul_count_ls)
## >> [['123-4567', 2], ['321-5487', 'No duplicates'], ['456-8792', 'No duplicates'], ['987-6542', 'No duplicates']]
mul_count_ls.sort(key=lambda x: x[0], reverse=True)     ## 리스트 내에서 첫 번째 인덱스로 내림차순 정렬해라
print(mul_count_ls)
## >> [['987-6542', 'No duplicates'], ['456-8792', 'No duplicates'], ['321-5487', 'No duplicates'], ['123-4567', 2]]

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
with open("jtbcnews_facebook_2018-01-24_2018-01-25.JSon", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)
    data = data.get('data')
    Jtbc_News(data)

######################## [ver2] ver1을 그냥 sort(), reverse()만 써서 간략화 함
data = []
with open("jtbcnews_facebook_2018-01-24_2018-01-25.JSon", encoding='UTF8') as json_file:
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