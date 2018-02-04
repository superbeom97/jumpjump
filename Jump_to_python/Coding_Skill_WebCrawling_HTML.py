####################################### <a href="~~" title="~~"> 처럼 하나의 < > 안에 있는 속성 빼내는 법 #######################################

################# 네이버 랭킹뉴스에서 Top 1~20위 뉴스의 제목과 링크만 뽑아내기
import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
import time

yyyymmdd = time.strftime("%Y%m%d")      ## 현재 연도, 달, 일

html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=000&date=%s' % yyyymmdd)     ## 웹크롤링 할 주소
soup = BeautifulSoup(html,'html.parser')        ## html(웹크롤링 할 주소)에 있는 모든 소스코드를 따오는

tag = soup.dt       ## 가장 먼저 나오는 soup(모든 소스코드)의 <dt>를 불러와 tag에 담음
print(tag)
## >> ## >> <dt><a href="/main/ranking/read.nhn?mid=etc&amp;sid1=111&amp;rankingType=popular_day&amp;oid=005&amp;
# aid=0001070647&amp;date=20180204&amp;type=1&amp;rankingSectionId=000&amp;rankingSeq=1"
# title="[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견">[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견</a></dt>

ass = tag.a        ## 그 <dt>에서 <a>를 ass에 담음
print(ass)
## >> <a href="/main/ranking/read.nhn?mid=etc&amp;sid1=111&amp;rankingType=popular_day&amp;oid=005&amp;
# aid=0001070647&amp;date=20180204&amp;type=1&amp;rankingSectionId=000&amp;rankingSeq=1"
# title="[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견">[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견</a>

print(ass['href'])
## soup.dt.a에서 'href=' 부분을 뽑아라 // <a href='' title=''> 처럼 a와 href, title이 하나의 < > 안에 있을 때, a['href'] 식으로 뽑아야 하는!!
## >> /main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=005&aid=0001070647&date=20180204&type=1&rankingSectionId=000&rankingSeq=1

print(ass['title'])     ## soup.dt.a에서 'title=' 부분을 뽑아라
## >> [단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견


########### 이 단계별 과정을 한 번에 적으면 soup.dt.a['title']
print(soup.dt.a['title'])
## >> [단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견


############ 근데 위에처럼 하면, 여러 개의 뉴스를 가져오지 못하고 <dt>가 가장 먼저 나오는 첫 번째 뉴스만 가져옴
########## -> <dt>보다 상위인 <li>를 가져 와서 그 중에서 <a>를 가져오면 됨

##  <li class="num1">

##			<div class="thumb"><a href="/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=005&aid=0001070647&date=20180204&type=1&rankingSectionId=000&rankingSeq=1"  title="[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견" ><img  src="http://imgnews.naver.net/image/thumb70/005/2018/02/04/1070647.jpg" title="[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견"  onError="javascript:this.src='http://imgnews.naver.net/image/news/2009/noimage_70x50.gif';" alt=""></a></div>

##			<dl>
##			<dt><a href="/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=005&aid=0001070647&date=20180204&type=1&rankingSectionId=000&rankingSeq=1"  title="[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견">[단독] 지금도 계속되는 ‘현대판 노예’… 경북 농가서 발견</a></dt>
##			<dd> 사진=국민일보DB23년간 임금 한푼 못 받은 60대  면사무소 학대의심 신고로 구출  컨테이너서 자며 축사관리 혹사…<span>

##				<span class="ico"><img src="http://static.news.naver.net/image/news/2017/07/12/ico_photo.gif" width="13" height="13" alt="포토" title="포토"></span>

##			국민일보</span> <span class="bar">|</span> <span class="num">2018.02.04</span></dd>
##			</dl>
##		</li>

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
    each_today_news_info = soup.find('li', attrs={'class':'num%s' % news_num})      ## 1~3위는 <li class="num1">

    Response_News()

    if news_num == 3: break     ## 1~3위까지는 <li class="num1"> 이니까 3위까지 뽑고 break

while True:
    news_num += 1
    each_today_news_info = soup.find('li', attrs={'class': 'gnum%s' % news_num})    ## 4위부터는 <li class="gnum4"> 로 되어 있음

    Response_News()

    if news_num == 20: break    ## 20위까지 뽑을 거니까 20번째가 되면 break