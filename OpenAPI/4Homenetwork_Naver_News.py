print("STRAT~~")
import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
import time

yyyymmdd = time.strftime("%Y%m%d")

html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=000&date=%s' % yyyymmdd)
soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

# movie_names = soup.findAll('div', attrs={'class':'tit3'})
# movie_changes = soup.findAll('td', attrs={'class':'range ac'})

# today_news_title = soup.findAll('dl')
# today_news_link = soup.findAll('dl', attrs={'dt':'href'})

# news_count = 0
# for each_news in today_news_title:
#     news_count += 1
#     # print(each_news)
#     # print("")
#     # print(type(each_news))
#     if news_count == 1: break


##########################################
tag = soup.dt
ass = tag.a
print(ass['href'])
print(ass['title'])
