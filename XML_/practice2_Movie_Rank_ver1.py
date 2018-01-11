import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from pandas import DataFrame                ## HTML로 바꾼 코드를 테이블을 만들어 csv 파일로 저장해라

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

movie_names = soup.find_all('div', attrs={'class':'tit3'})
movie_changes = soup.find_all('td', attrs={'class':'range ac'})
movie_changes_result = []
for movie_change in movie_changes:
    td_movie_change = list(movie_change.strings)
    movie_changes_result.append(td_movie_change[0])

movie_name_result = []
rank = 1
movie_changes_index = 0
for movie_name in movie_names:
    td_movie_name = list(movie_name.strings)
    td_movie_name[0] = rank
    movie_chg = movie_changes_result[int("%s" % movie_changes_index)]
    td_movie_name[2] = movie_chg
    movie_name_result.append(td_movie_name)
    rank += 1
    movie_changes_index += 1

movie_table = DataFrame(movie_name_result, columns=('순위','영화명','변동폭'))
movie_table.to_csv("movie_table.csv", encoding="cp949", mode='w', index=False)
## index=True 하면 csv 파일에서 첫 번째 열에 순서가 나오는 0~
## index=False 하면 순서 나오는 첫 번째 열을 없애 줌