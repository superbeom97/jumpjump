import urllib.request
from bs4 import BeautifulSoup


html = urllib.request.urlopen('http://tv.naver.com/r/')
soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

print("")
print("<< 현재 인기 클립 영상 상위 1 ~ 20위 목록입니다:) 관심 있는 영상은 바로 가기를 클릭해 주세요~ >>\n".center(75))

video_link_group = soup.findAll('a')      ## 링크가 포함되어 있는 <a>의 모든 정보 가져오기 - 1~3위 링크 뽑기 위해

## <div class="cds_type"> 에 포함되어 있는 소스코드를 가져오는 - 4~20위 링크 뽑기 위해
## 4~20위는 <a> 안에 주소가 2개 포함되어 있어 동일한 주소가 두 번씩 출력 되는
## 그래서 그 보다 하위인 <div class="cds_type"> 소스코드 모두 가져옴
today_video_lowlink = soup.findAll('div', attrs={'class':'cds_type'})     ## 1~3위랑 4~20위의 범위를 다르게 잡아 줌


video_num = 0
for each_video in video_link_group:             ## 1-3위 - 링크가 포함되어 있는 <a>의 모든 정보에서
    check_link = each_video.get('href')         ## 링크 부분인 'href'만 가져오기
    if "http://tv.naver.com/v/" in check_link:  ## 링크에 순위 동영상 외 다른 동영상 링크도 포함되어 있어, 순위 동영상 링크 가져오기
        video_num += 1                          ## 순위 동영상에는 "http://tv.naver.com/v/"이 포함되어 있음
        print("<< %s 위 >>" % video_num)
        print("제목 : %s" % each_video.img.get('alt'))  ## <a> 하위 <img alt="이세영, 이승기의 영혼 조정! 이제 영원히 날 지키게 될 거예요"> 에서 제목 뽑아내기
        print("바로 가기 ☞  %s\n" % check_link)        ## <a href="http://tv.naver.com/v/2659359/list/67096"> 에서 링크 뽑아내기
    if video_num == 3: break

for each_video in today_video_lowlink:          ## 4~20위 - <div class="cds_type"> 소스코드를 하나씩 넣음
    check_link = each_video.a.get('href')
    if "http://tv.naver.com/v/" in check_link:
        video_num += 1
        print("<< %s 위 >>" % video_num)
        print("제목 : %s" % each_video.img.get('alt'))  ## <div class="cds_type"> 하위 <img alt="이세영, 이승기의 영혼 조정! 이제 영원히 날 지키게 될 거예요"> 에서 제목 뽑아내기
        print("바로 가기 ☞  %s\n" % check_link)        ## <dl class="cds_info"> 하위 <a href="http://tv.naver.com/v/2659232/list/67096"> 에서 링크 뽑아내기
    if video_num == 20: break

