import operator

print("--------------------------------------------------------------")
print("<<simple dictionary sorting>>".center(50))
dic_fir = {'라희':80, '가수':90, '다영':60}
print(dic_fir)
## >> {'라희': 80, '가수': 90, '다영': 60}

print('<<딕셔너리 - VALUE로 정렬>>'.center(44))
dic_snd = sorted(dic_fir.items(), key=operator.itemgetter(1))   ## 딕셔너리 dic_fir의 value로 정렬해라
print(dic_snd)
## >> [('다영', 60), ('라희', 80), ('가수', 90)]

dic_thrd = sorted(dic_fir.items(), key=operator.itemgetter(1), reverse=True) ## 딕셔너리 dic_fir의 value로 내림차순 정렬해라
print(dic_thrd)
## >> [('가수', 90), ('라희', 80), ('다영', 60)]

print("<<딕셔너리 - KEY로 정렬>>".center(42))
dic_snd = sorted(dic_fir.items(), key=operator.itemgetter(0))   ## 딕셔너리 dic_fir의 key로 정렬해라
print(dic_snd)
## >> [('가수', 90), ('다영', 60), ('라희', 80)]

dic_thrd = sorted(dic_fir.items(), key=operator.itemgetter(0), reverse=True) ## 딕셔너리 dic_fir의 key로 내림차순 정렬해라
print(dic_thrd)
## >> [('라희', 80), ('다영', 60), ('가수', 90)]

print("--------------------------------------------------------------")
print("<<tuple 배열로 이뤄진 딕셔너리를 정렬하기>>".center(50))
data = {}
data['라희'] = (80, 95, 90)
data['가수'] = (90, 80, 70)
data['다영'] = (70, 100, 90)
print(data)
## >> {'라희': (80, 95, 90), '가수': (90, 80, 70), '다영': (70, 100, 90)}

##### sorted(data.items(), key=lambda x: x[1][0], reverse=False)
##### sort(1, 2, 3) -> 첫 번째 iteratable 파라미터가 하니식 2번째 수식에 대입되어 돌아 간다.
print('<<tuple의 첫 번째 항목으로 정렬>>'.center(50))
data_snd = sorted(data.items(), key=lambda x: x[1][0], reverse=False)   ## x[1][0] : 딕셔너리에서 [1] 즉, value 값 중 [0] 첫 번째 인덱스!! 를 기준으로 정렬
## data_snd = sorted(data.items(), key=lambda x: x[1][1], reverse=False)   ## x[1][1] : 딕셔너리에서 [1] 즉, value 값 중 [1] 즉, 두 번째 인덱스!! 를 기준으로 정렬
## data_snd = sorted(data.items(), key=lambda x: x[0][0], reverse=False)   ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_snd)
## >> [('다영', (70, 100, 90)), ('라희', (80, 95, 90)), ('가수', (90, 80, 70))]

print('<<tuple의 두 번째 항목으로 정렬>>'.center(50))
data_thrd = sorted(data.items(), key=lambda x: x[1][1], reverse=False)
print(data_thrd)
## >> [('가수', (90, 80, 70)), ('라희', (80, 95, 90)), ('다영', (70, 100, 90))]

print('<<tuple의 세 번째 항목으로 정렬>>'.center(50))
data_four = sorted(data.items(), key=lambda x: x[1][2], reverse=False)
print(data_four)
## >> [('가수', (90, 80, 70)), ('라희', (80, 95, 90)), ('다영', (70, 100, 90))]

print("--------------------------------------------------------------")
print("<<dictionary 배열로 이뤄진 딕셔너리를 정렬하기>>".center(50))
data['라희'] = {'국어':80, '수학':95, '영어':80}
data['가수'] = {'국어':90, '수학':80, '영어':70}
data['다영'] = {'국어':70, '수학':100, '영어':90}
print(data)
## >> {'라희': {'국어': 80, '수학': 95, '영어': 80}, '가수': {'국어': 90, '수학': 80, '영어': 70}, '다영': {'국어': 70, '수학': 100, '영어': 90}}

print('<<국어 성적으로 정렬>>'.center(44))
data_snd = sorted(data.items(), key=lambda x: x[1]['국어'], reverse=False)    ## x[1]['국어'] : 딕셔너리에서 [1] 즉, value 값 중 '국어'의 value를 기준으로 정렬
print(data_snd)
## >> [('다영', {'국어': 70, '수학': 100, '영어': 90}), ('라희', {'국어': 80, '수학': 95, '영어': 80}), ('가수', {'국어': 90, '수학': 80, '영어': 70})]

print('<<영어 성적으로 정렬>>'.center(44))
data_thrd = sorted(data.items(), key=lambda x: x[1]['영어'], reverse=False)   ## x[1]['영어'] : 딕셔너리에서 [1] 즉, value 값 중 '영어'의 value를 기준으로 정렬
print(data_thrd)
## >> [('가수', {'국어': 90, '수학': 80, '영어': 70}), ('라희', {'국어': 80, '수학': 95, '영어': 80}), ('다영', {'국어': 70, '수학': 100, '영어': 90})]

print('<<이름 순으로 정렬>>'.center(44))
data_thrd.sort(key=lambda x: x[0][0], reverse=False)  ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_thrd)

data_four = sorted(data.items(), key=lambda x: x[0][0], reverse=False)  ## x[0][0] : 딕셔너리에서 [0] 즉, key 값 중 [0] 즉, 첫 번째 인덱스!! 를 기준으로 정렬
print(data_four)