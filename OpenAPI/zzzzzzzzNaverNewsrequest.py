########################### 요리 레시피 추천 - 네이버 블로그 기반

import urllib.request
import json

client_id = "R1JCmA0iVfg4x_ecHHkN"
client_secret = "EycJ4UgDEA"

print("<< 요리 레시피 검색 모드입니다:) >>".center(30))
inp_want_food = input("레시피 검색을 원하는 요리 이름을 입력해 주세요 : ")

want_food = urllib.parse.quote(inp_want_food)
recipe_food = urllib.parse.quote(" 레시피")
research_food = want_food + recipe_food
display_recipe = "10"    ## 검색 결과 출력 건수 지정 - 10 ~ 100
page_recipe = "50"        ## 검색 시작 위치로 최대 1000까지 가능 - 1 ~ 1000
sort_recipe = "sim"     ## 정렬 옵션 : sim (유사도순), date (날짜순)

end_point = "https://openapi.naver.com/v1/search/blog"

parameters = "?query=" + research_food      ## 검색을 원하는 문자열로서 UTF-8로 인코딩
parameters += "&display=" + display_recipe   ## 검색 결과 출력 건수 지정
parameters += "&sim=" + sort_recipe   ## 정렬 옵션 : sim (유사도순), date (날짜순)

url = end_point + parameters

req = urllib.request.Request(url)

req.add_header("X-Naver-Client-Id",client_id)
req.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(req)
rescode = response.getcode()

if(rescode==200):
    jsonResult = json.loads(response.read().decode('utf-8'))

    with open('%s_recipe_naver_블로그.json' % inp_want_food, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(str_)
        print('%s_recipe_naver_블로그.json SAVED' % inp_want_food)

else:
    print("Error Code:" + rescode)

recipe_blog_ls = []
with open("%s_recipe_naver_블로그.json" % inp_want_food, encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    recipe_blog_ls = json.loads(json_string)

for change_str in recipe_blog_ls.get('items'):
    ########## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업
    if '<b>' in change_str.get('title') or '</b>' in change_str.get('title'):
        change_str['title'] = change_str.get('title').replace("<b>", "")
        change_str['title'] = change_str.get('title').replace("</b>", "")
    if '<b>' in change_str.get('description') or '</b>' in change_str.get('description'):
        change_str['description'] = change_str.get('description').replace('<b>', "")
        change_str['description'] = change_str.get('description').replace('</b>', "")

    ########## 링크 주소가 잘못 나와서 다시 조합하는 작업
    change_str['link'] += "z"   ## link에 나와 있는 마지막 12자리 숫자를 가져오기 위해 z를 마지막에 넣어 줌
    new_link = change_str.get('bloggerlink') + "/" + change_str.get('link')[-13:-1]   ## z가 없으면 마지막 숫자는 누락되니까(-1번째 자리는 포함 안 하니까)
    change_str['link'] = new_link   ## 새로운 link 주소를 입력해 줌

with open("%s_recipe_naver_블로그.json" % inp_want_food, 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(recipe_blog_ls, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

print("<< %s 레시피 추천 목록입니다:) 관심 있는 레시피를 클릭해 주세요~ >>".center(55) % inp_want_food)
for prn_recipe in recipe_blog_ls.get('items'):
    print("\n<<제목>>\n%s\n" % prn_recipe.get('title'))
    print("<<간략 소개>>\n%s\n" % prn_recipe.get('description'))
    print("바로 가기 ☞  %s\n" % prn_recipe.get('link'))
    print("=" * 150)

