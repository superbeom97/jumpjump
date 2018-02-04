###################################### 네이버 실시간 뉴스 랭킹 Web Crawling

import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
import time

yyyymmdd = time.strftime("%Y%m%d")

html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=000&date=%s' % yyyymmdd)
soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

def Response_News():
    news_title_link = each_today_news_info.a
    print("<< %s 위 >>" % news_num)
    print("제목 : %s" % news_title_link['title'])
    print("바로 가기 ☞ http://news.naver.com%s\n" % news_title_link['href'])

    ######## 또는 news_title_link로 새롭게 변수 지정할 필요 없이
    # print("<< %s 위 >>" % news_num)
    # print("제목 : %s" % each_today_news_info.a['title'])      ## 바로 each_today_news_info.a['title']) 이렇게 뽑아 내도 됨
    # print("바로 가기 ☞ http://news.naver.com%s\n" % each_today_news_info.a['href'])

news_num = 0
while True:
    news_num += 1
    each_today_news_info = soup.find('li', attrs={'class':'num%s' % news_num})

    Response_News()

    if news_num == 3: break

while True:
    news_num += 1
    each_today_news_info = soup.find('li', attrs={'class': 'gnum%s' % news_num})

    Response_News()

    if news_num == 20: break