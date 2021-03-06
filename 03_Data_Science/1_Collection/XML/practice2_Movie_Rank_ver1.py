import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from pandas import DataFrame                ## HTML로 바꾼 코드를 테이블을 만들어 csv 파일로 저장해라

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

movie_names = soup.findAll('div', attrs={'class':'tit3'})
movie_changes = soup.findAll('td', attrs={'class':'range ac'})

movie_changes_result = []
for movie_change in movie_changes:
    # td_movie_change = list(movie_change.strings)
    td_movie_change = list(movie_change)    ## 이건 strings 필요 없는 듯!!
    movie_changes_result.append(td_movie_change[0])

movie_name_result = []
rank = 1
movie_changes_index = 0
for movie_name in movie_names:
    td_movie_name = list(movie_name.strings)
    td_movie_name[0] = rank
    td_movie_name[2] = movie_changes_result[movie_changes_index]
    movie_name_result.append(td_movie_name)
    rank += 1
    movie_changes_index += 1

movie_table = DataFrame(movie_name_result, columns=('순위','영화명','변동폭'))
movie_table.to_csv("movie_table.csv", encoding="cp949", mode='w', index=False)
## index=True 하면 csv 파일에서 첫 번째 열에 순서가 나오는 0~
## index=False 하면 순서 나오는 첫 번째 열을 없애 줌

# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.