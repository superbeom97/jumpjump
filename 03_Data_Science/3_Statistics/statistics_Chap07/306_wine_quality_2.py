### 7.2 와인 품질 데이터셋 - 2 그룹화, 히스토그램, t 검정
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

## 1 기술 통계
# 데이터셋을 팬더스 데이터프레임으로 읽기
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

# 변수별 요약통계 표시
print(wine.describe())

# 유일값 찾기
print(sorted(wine.quality.unique()))

# 빈도 계산
print(wine.quality.value_counts())


### 2 그룹화, 히스토그램, t 검정
## 레드와 화이트 와인을 구분해 통계량을 살펴보자.

# 와인 종류에 따른 기술 통계를 출력하기
print(wine.groupby('type')[['quality']].describe().unstack('type'))     ## 레드와 화이트 와인을 구분하여 quality 열의 요약통계를 출력
## groupby() : type 열의 두 값, 즉 레드와 화이트를 기준으로 데이터셋을 그룹화, 대괄호 [] 사용
## describe() : quality 열의 요약통계를 두 그룹으로 구분하여 세로 방향으로 출력
## unstack() : 그 결과를 가로 방향으로 재구조화

# 특정 사분위수 계산하기
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
## quantile() : quality 열의 25번째와 75번째 백분위 수를 출력

# 와인 종류에 따른 품질의 분포 확인하기
# ↳ 와인별로 히스토그램을 그려보고, 와인 종류에 따라 품질의 차이가 있는지 검정해보자.
red_wine = wine.ix[wine['type']=='red', 'quality']
white_wine = wine.ix[wine['type']=='white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color="white", label="White wine"))
plt.xlabel("Quality Score")
plt.ylabel("Density")           ## x, y축 라벨링(이름 붙이기)
plt.title("Distribution of Quality by Wine Type")   ## 제목 붙이기
plt.legend()    ## 그래프 상의 범례를 나타냄
plt.show()

# 와인 종류에 따라 품질의 차이 검정 - 와인 종류에 따른 품질의 차이가 통계적으로 유의한지 알기 위해 t 검정 실시
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))  ## groupby(), agg() : 그룹별 품질의 평균과 표준편차를 구한다.
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))