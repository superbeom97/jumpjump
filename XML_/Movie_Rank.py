import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')        ## 모든 소스코드를 따오는

movie_names = soup.find_all('div', attrs={'class':'tit3'})
movie_changes = soup.find_all('td', attrs={'class':'range ac'})
a_result = []
for z in movie_changes:
    td_z = list(z.strings)
    a_result.append(td_z[0])
# a_result = a_result[]

movie_name_result = []
rank = 1
while True:
    for movie_name in movie_names:
        td_movie_name = list(movie_name.strings)
        td_movie_name[0] = rank
        for movie_chg in a_result:
            td_movie_name[2] = movie_chg
            movie_name_result.append(td_movie_name)
            rank += 1
            break
    break

movie_table = DataFrame(movie_name_result, columns=('순위','영화명','변동폭'))
movie_table.to_csv("movie_table.csv", encoding="cp949", mode='w', index=False)