import urllib.request
from bs4 import BeautifulSoup

print("")
print("<< 음악 감상 모드입니다:) >>\n".center(40))
inp_want_music = input("듣고 싶은 노래 제목이나 가수 이름을 입력해 주세요 : ")

html = urllib.request.urlopen('https://www.youtube.com/results?search_query=%s' % urllib.parse.quote(inp_want_music))
soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

## 모든 소스코드에서 <h3 class="yt-lockup-title "> 하위 소스코드만 따오는
music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})

print("")
print("<< '%s' 노래 목록입니다:) 원하시는 노래는 바로 가기를 클릭해 주세요~ >>\n".center(65) % inp_want_music)

music_count = 0
while True:
    music_count += 1

    ## music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})가 리스트로 이루어져 있음
    ## 리스트에서 하나씩 뽑아 <a aria-describedby="description-id-841094" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CFkQ3DAYACITCJXFm4jrjdkCFQRYYAodGLMBsSj0JFIG7J2066Oo" dir="ltr" href="/watch?v=QLAmTkqzSPs" rel="spf-prefetch" title="이루 - 흰눈">이루 - 흰눈</a>
    print("제목 : %s" % music_info[music_count].a.get('title'))   ## <a>에 포함되어 있는 title="이루 - 흰눈"을 뽑아라
    print("바로 가기 ☞  https://www.youtube.com%s\n\n" % music_info[music_count].a.get('href'))     ## <a>에 포함되어 있는 href="/watch?v=QLAmTkqzSPs"를 뽑아라

    if music_count == 10: break     ## 노래 10개 추천하고 종료해라