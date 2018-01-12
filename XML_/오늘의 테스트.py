import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

movie_name = soup.findAll('div', attrs={'class':'tit3'})
change_rank = soup.findAll('td', attrs={'class':'range ac'})

change_rank_result = []
for change_rk in change_rank:
    td_change_rank = list(change_rk)
    change_rank_result.append(td_change_rank[0])

movie_name_result = []
rank = 1
change_rank_index = 0
for movie_nm in movie_name:
    td_movie_name = list(movie_nm.strings)
    td_movie_name[0] = rank
    # movie_chg = change_rank_result[change_rank_index]
    td_movie_name[2] = change_rank_result[change_rank_index]
    movie_name_result.append(td_movie_name)
    rank += 1
    change_rank_index += 1

movie_table = DataFrame(movie_name_result, columns=('순위', '영화명', '변동폭'))
movie_table.to_csv("movie_table.csv", encoding="cp949", mode='w', index=False)


# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.