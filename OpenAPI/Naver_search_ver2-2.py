import json
from pprint import pprint

total_news = []
with open("이명박_naver_news.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    total_news = json.loads(json_string)

for change_str in total_news:
    if '&quot;' in change_str.get('title') or '&lt;' in change_str.get('title') or '&gt;' in change_str.get('title') or '<b>' in change_str.get(
            'title') or '</b>' in change_str.get('title'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        new_npercend = change_str.get('title').replace("&quot;", "'")
        change_str['title'] = new_npercend
        new_npercend = change_str.get('title').replace("&lt;", "<")
        change_str['title'] = new_npercend
        new_npercend = change_str.get('title').replace("&gt;", ">")
        change_str['title'] = new_npercend
        new_npercend = change_str.get('title').replace("<b>", "")
        change_str['title'] = new_npercend
        new_npercend = change_str.get('title').replace("</b>", "")
        change_str['title'] = new_npercend
    if '&quot;' in change_str.get('description') or '&lt;' in change_str.get('description') or '&gt;' in change_str.get(
            'description') or '<b>' in change_str.get('description') or '</b>' in change_str.get(
            'description'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        new_npercend = change_str.get('description').replace('&quot;', "'")
        change_str['description'] = new_npercend
        new_npercend = change_str.get('description').replace('&lt;', "<")
        change_str['description'] = new_npercend
        new_npercend = change_str.get('description').replace('&gt;', ">")
        change_str['description'] = new_npercend
        new_npercend = change_str.get('description').replace('<b>', "")
        change_str['description'] = new_npercend
        new_npercend = change_str.get('description').replace('</b>', "")
        change_str['description'] = new_npercend

with open('change_이명박_naver_news.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(total_news, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

address_ls = []
for address_get in total_news:
    address = address_get.get('org_link')
    point_address = address.split('/')
    if len(point_address) >= 3:
        address_ls.append(point_address[2])

