## [ver2]   도메인별 기사건수 분석 - 내림차순으로
## [ver2-2] 이미 있는 JSon 파일을 읽어봐 정렬, 출력하는 버전
## [ver2-3] 리스트 내에서 int가 첫 번째가 아닌 다른 자리에 있어도, 정렬하는 법 적용

## 출력 예시)
## [도메인별 기사건수 분석]
## >> 'www.anewsa.com' : 132 건
## >> 'www.chosun.com' : 98 건

import json
from pprint import pprint

total_news = []
with open("이명박_naver_news.JSon", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    total_news = json.loads(json_string)

for change_str in total_news:
    if '&quot;' in change_str.get('title') or '&lt;' in change_str.get('title') or '&gt;' in change_str.get('title') or '<b>' in change_str.get(
            'title') or '</b>' in change_str.get('title'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        change_str['title'] = change_str.get('title').replace("&quot;", "'")
        change_str['title'] = change_str.get('title').replace("&lt;", "<")
        change_str['title'] = change_str.get('title').replace("&gt;", ">")
        change_str['title'] = change_str.get('title').replace("<b>", "")
        change_str['title'] = change_str.get('title').replace("</b>", "")
    if '&quot;' in change_str.get('description') or '&lt;' in change_str.get('description') or '&gt;' in change_str.get(
            'description') or '<b>' in change_str.get('description') or '</b>' in change_str.get(
            'description'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        change_str['description'] = change_str.get('description').replace('&quot;', "'")
        change_str['description'] = change_str.get('description').replace('&lt;', "<")
        change_str['description'] = change_str.get('description').replace('&gt;', ">")
        change_str['description'] = change_str.get('description').replace('<b>', "")
        change_str['description'] = change_str.get('description').replace('</b>', "")

with open('change_이명박_naver_news.JSon', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(total_news, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

address_ls = []
for address_get in total_news:
    address = address_get.get('org_link')
    point_address = address.split('/')
    if len(point_address) >= 3:
        address_ls.append(point_address[2])

address_number  = []
only_one = set()
for check_address in address_ls:
    each_ls = []
    each_ls.append(check_address)
    each_ls.append(address_ls.count(check_address))
    address_number.append(each_ls)
    only_one.add(check_address)     ## set형은 .add()를 통해 추가함

final_ls = []
for check_mul in only_one:
    for mul in address_number:
        if check_mul in mul:
            final_ls.append(mul)
            break

########################## 리스트 내에서의 정렬
# score = [("개", 50), ("기린", 100), ("고양이", 30)]
# score.sort(key=lambda x: x[1])
# print(score)
# >> [("고양이", 30), ("개", 50), ("기린", 100)]


# final_ls.sort(key=lambda k: k[1])                 ## final_ls를 오름차순으로 정렬
final_ls.sort(key=lambda k: k[1], reverse=True)     ## reverse=True를 붙여 주면, 내림차순으로 정렬

news_count = 0
for prnt in final_ls:
    news_count += prnt[1]
    print(">> '%s' : %s 건" % (prnt[0], prnt[1]))
print("\n>> 실제 뉴스 총 건수 : %s" % len(address_number))     ## 받아들인 뉴스가 모아져 있는 리스트 내의 갯수를 통해
print(">> 검색한 뉴스 총 건수 : %s" % news_count)   ## 중복 도메인의 수의 총합을 통해 확인


# sorted_num_of_domain_info = sorted(domain_info_list, key=lambda k: k[1],reverse=True)