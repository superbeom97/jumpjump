### 네이버에서 검색해서 json 파일로 저장하는 코드

## [ver1]   json 파일에서 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
## [ver2]   도메인별 기사건수 분석 - 내림차순으로
## 출력 예시)
## [도메인별 기사건수 분석]
## >> 'www.anewsa.com' : 132 건
## >> 'www.chosun.com' : 98 건

## [참고 사항]
## - API 호출 수 25,000회/일로 제한
## - 한 번 호출에 최대 100개 검색
## - 한 번 실행에 최대 1000개까지 기사 검색

import urllib.request
import datetime
import json

app_id = "4fLRRIHMFwAI53sYeHJu"
app_pw = "gvsFISGKOs"


def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getNaverSearchResult(sNode, search_text, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode

    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)
    url = base + node + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def getPostData(post, jsonResult):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title': title, 'description': description, 'org_link': org_link, 'pDate': pDate})


def main():
    jsonResult = []

    sNode = 'news'
    search_text = '이명박'
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    index = 1  ## 1번 루프를 돌 때마다 100건이 조회되기 때문에 1000번을 넘기지 않게 하기 위한 인덱스임
    while ((jsonSearch != None) and (jsonSearch['display'] != 0) and index < 9):
        for post in jsonSearch['items']:
            if '&quot;' in post.get('title'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
                new_npercend = post.get('title').replace("&quot;", "'")
                post['title'] = new_npercend
            if '&quot;' in post.get('description'):
                new_npercend = post.get('description').replace('&quot;', "'")
                post['description'] = new_npercend
            getPostData(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        # index += 1
        index = index + 1

        with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)

        print("%s_naver_%s.json SAVED" % (search_text, sNode))
        Sort_Print(search_text, sNode)

def Sort_Print(search_text, sNode):
    total_news = []
    with open("%s_naver_%s.json" % (search_text, sNode), encoding='UTF8') as json_file:
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

    with open('change_이명박_naver_news.json', 'w', encoding='utf8') as outfile:
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
        each_ls.append(address_ls.count(check_address))
        each_ls.append(check_address)
        address_number.append(each_ls)
        only_one.add(check_address)   ## set형은 .add()를 통해 추가함

    final_ls = []
    for check_mul in only_one:
        for mul in address_number:
            if check_mul in mul:
                final_ls.append(mul)
                break

    final_ls.sort()
    final_ls.reverse()

    news_count = 0
    for prnt in final_ls:
        news_count += prnt[0]
        print(">> '%s' : %s 건" % (prnt[1], prnt[0]))
    print("\n>> 실제 뉴스 총 건수 : %s" % len(address_number))     ## 받아들인 뉴스가 모아져 있는 리스트 내의 갯수를 통해
    print(">> 검색한 뉴스 총 건수 : %s" % news_count)   ## 중복 도메인의 수의 총합을 통해 확인


if __name__ == '__main__':
    main()