import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

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
while True:
    for movie_name in movie_names:
        td_movie_name = list(movie_name.strings)
        td_movie_name[0] = rank
        movie_chg = movie_changes_result[int("%s" % movie_changes_index)]
        td_movie_name[2] = movie_chg
        movie_name_result.append(td_movie_name)
        rank += 1
        movie_changes_index += 1
    break

movie_table = DataFrame(movie_name_result, columns=('순위','영화명','변동폭'))
movie_table.to_csv("movie_table.csv", encoding="cp949", mode='w', index=False)