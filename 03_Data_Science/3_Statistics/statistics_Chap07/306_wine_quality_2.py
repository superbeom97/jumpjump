## 두 개의 파일, 레드 와인과 화이트 와인으로 구성
## 11개의 입력 변수와 1개의 출력 변수로 구성
## 출력 변수는 quality(와인 품질 평가 점수) 변수로서 0점(가장 낮은 품질)에서 10점(가장 높은 품질) 사이의 점수를 갖는다.
## 입력 변수 11개는 와인의 물리화학적 특성이다.

###################################### 7.2 와인 품질 데이터셋 - 1 기술 통계
## 데이터셋의 각 열에 대한 요약통계를 살펴보고 출력 변수인 quality 열의 유일값들을 찾고, 각 값에 대한 관측값 개수를 구해 보자.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm


##################################### 데이터셋을 팬더스 데이터프레임으로 읽기    ## ↱ 필드 구분 기호를 쉼표(sep=',')로 지정 // header=0 : 열 헤더를 파일 첫 행으로 지정
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)   ## pandas의 read_csv() 함수를 사용하여 CSV 파일을 읽어 데이터프레임에 넣는다.
wine.columns = wine.columns.str.replace(' ', '_')   ## 열 헤더에 포함되어 있는 공백을 밑줄로 바꾼다(fixed acidity -> fixed_acidity)
print(wine.head())  ## head() : 헤더 행과 처음 5개 행을 출력 -> () 안에 숫자를 넣으면, 그 숫자만큼 출력


##################################### 변수별 요약통계 표시
print(wine.describe())  ## describe() : 수치형 변수들에 대한 요약통계를 출력
# ↳ 관측값 개수(count), 평균(mean), 표준편차(std), 최솟값(min)
#   25번째 백분위 수(25%), 중앙값(50%), 75번째 백분위 수(75%), 최댓값(max)


##################################### 유일값 찾기
print(sorted(wine.quality.unique()))    ## quality.unique() : 유일값 출력


##################################### 빈도 계산
print(wine.quality.value_counts())    ## quality.value_counts() : 유일값별 관측값 개수를 내림차순으로 정렬하여 출력



###################################### 2 그룹화, 히스토그램, t 검정
## 레드와 화이트 와인을 구분해 통계량을 살펴보자.


##################################### 와인 종류에 따른 기술 통계를 출력하기
print(wine.groupby('type')[['quality']].describe().unstack('type'))     ## 레드와 화이트 와인을 구분하여 quality 열의 요약통계를 출력
# print(wine.groupby('type').describe())     ## 레드와 화이트 와인을 구분하여, 모든 열의 요약통계를 출력
# print(wine.groupby('type')['quality'].describe())       ## 레드와 화이트 와인을 구분하여, quality 열의 요약통계를 출력 - 출력물에 quality 명시 x
# print(wine.groupby('type')[['quality']].describe())     ## 레드와 화이트 와인을 구분하여, quality 열의 요약통계를 출력 - 출력물에 quality 명시 o
# print(wine.groupby('type')[['quality']].describe().unstack())               ## unstack() = unstack('type') = unstack('quality') 다 똑같음
# print(wine.groupby('type')[['quality']].describe().unstack('quality'))      ## unstack() = unstack('type') = unstack('quality') 다 똑같음
# print(wine.groupby('type')[['pH']].describe())            ## 레드와 화이트 와인을 구분하여, pH 열의 요약통계를 출력 - 출력물에 pH 명시 o
## groupby() : type 열의 두 값, 즉 레드와 화이트를 기준으로 데이터셋을 그룹화, 대괄호 [] 사용
## describe() : quality 열의 요약통계를 두 그룹으로 구분하여 세로 방향으로 출력
## unstack() : 결과를 가로 방향으로 재구조화


##################################### 특정 사분위수 계산하기
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# print(wine.groupby('type')[['quality']].quantile().unstack('type'))     ## quantile() : 50번째 백분위수 출력 = quantile(0.5)
# print(wine.groupby('type')[['quality']].quantile([0, 0.25, 0.5, 0.75, 1]).unstack('type'))
## quantile() : 백분위수 출력


##################################### 와인 종류에 따른 품질의 분포 확인하기
############# ↳ 와인별로 히스토그램을 그려보고, 와인 종류에 따라 품질의 차이가 있는지 검정해보자.
red_wine = wine.ix[wine['type']=='red', 'quality']          ## DataFrame.ix[행, 열] -> wine['type']=='red'인 행에서 quality 열을 선택
white_wine = wine.ix[wine['type']=='white', 'quality']      ## DataFrame.ix[행, 열] -> wine['type']=='white'인 행에서 quality 열을 선택
# sns.set_style("dark")           ## set_style([style,rc]) : Set the aesthetic style of the plots - darkgrid, whitegrid, dark, white, ticks
# sns.set_style("whitegrid")    ## set_style([style,rc]) : Set the aesthetic style of the plots - darkgrid, whitegrid, dark, white, ticks
# sns.set_style("dark") = sns.set(style="dark")
print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color="white", label="White wine"))
plt.xlabel("Quality Score")
plt.ylabel("Density")           ## x, y축 라벨링(이름 붙이기)
plt.title("Distribution of Quality by Wine Type")   ## 제목 붙이기
plt.legend()    ## 그래프 상의 범례를 나타냄
plt.show()


# ##################################### 와인 종류에 따라 품질의 차이 검정 - 와인 종류에 따른 품질의 차이가 통계적으로 유의한지 알기 위해 t 검정 실시
# print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))  ## groupby(), agg() : 그룹별 품질의 평균과 표준편차를 구한다.
# tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))