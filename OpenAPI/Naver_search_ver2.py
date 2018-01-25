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
    address_ls = []
    while ((jsonSearch != None) and (jsonSearch['display'] != 0) and index < 9):
        for post in jsonSearch['items']:
            if '&quot;' in post.get('title') or '&lt;' in post.get('title') or '&gt;' in post.get('title') or '<b>' in post.get('title') or '</b>' in post.get('title') :  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
                new_npercend = post.get('title').replace("&quot;", "'")
                post['title'] = new_npercend
                new_npercend = post.get('title').replace("&lt;", "<")
                post['title'] = new_npercend
                new_npercend = post.get('title').replace("&gt;", ">")
                post['title'] = new_npercend
                new_npercend = post.get('title').replace("<b>", "")
                post['title'] = new_npercend
                new_npercend = post.get('title').replace("</b>", "")
                post['title'] = new_npercend
            if '&quot;' in post.get('description') or '&lt;' in post.get('description') or '&gt;' in post.get('description') or '<b>' in post.get('description') or '</b>' in post.get('description') :  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
                new_npercend = post.get('description').replace('&quot;', "'")
                post['description'] = new_npercend
                new_npercend = post.get('description').replace('&lt;', "<")
                post['description'] = new_npercend
                new_npercend = post.get('description').replace('&gt;', ">")
                post['description'] = new_npercend
                new_npercend = post.get('description').replace('<b>', "")
                post['description'] = new_npercend
                new_npercend = post.get('description').replace('</b>', "")
                post['description'] = new_npercend
            getPostData(post, jsonResult)

            try:
                address = post.get('originallink')
                point_address = address.split('/')
                if point_address[2]:
                    address_ls.append(point_address[2])
            except:
                pass

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        # index += 1
        index = index + 1

        with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)

        print("%s_naver_%s.json SAVED" % (search_text, sNode))

    print("\n[[도메인별 기사건수 분석]]")
    new_address = []
    index_count = -1
    for compa in address_ls:
        personal_address = []
        index_count += 1
        if index_count == len(address_ls) - 1:
            break
        count_num = 0
        for next_compa in address_ls[(index_count):]:
            if compa == next_compa:
                count_num += 1
                if (index_count+1) == len(address_ls):
                    break
                del address_ls[(index_count + 1)]
        personal_address.append(count_num)
        personal_address.append(compa)
        new_address.append(personal_address)

    new_address.sort()
    new_address.reverse()

    change_num_index = -1
    for step_by in new_address:
        change_num_index += 1
        if change_num_index == len(new_address) - 1:  ## step_by가 리스트 change_num_ls의 마지막 자릿 수인지 확인
            break  ## step_by가 리스트 change_num_ls의 마지막 자릿 수 일 때는 비교 대상이 없으니, 종료해라
        del_index = 0
        for next_step_by in new_address[(change_num_index + 1):]:  ## step_by 다음 인덱스들을 가져오는 코드 ↴
            del_index += 1
            if step_by[1] == next_step_by[1]:
                step_by[0] = step_by[0] + next_step_by[0]
                del new_address[del_index]

    total_news = 0
    for prn in new_address:
        total_news += prn[0]
        print(">> '%s' : %s 건" % (prn[1], prn[0]))
    print("\n>> 총 뉴스 건수 : %s" % total_news)

if __name__ == '__main__':
    main()