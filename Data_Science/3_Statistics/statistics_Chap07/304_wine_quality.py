## 두 개의 파일, 레드 와인과 화이트 와인으로 구성
## 11개의 입력 변수와 1개의 출력 변수로 구성
## 출력 변수는 quality(와인 품질 평가 점수) 변수로서 0점(가장 낮은 품질)에서 10점(가장 높은 품질) 사이의 점수를 갖는다.
## 입력 변수 11개는 와인의 물리화학적 특성이다.

### 7.2 와인 품질 데이터셋 - 1 기술 통계
## 데이터셋의 각 열에 대한 요약통계를 살펴보고 출력 변수인 quality 열의 유일값들을 찾고, 각 값에 대한 관측값 개수를 구해 보자.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 데이터셋을 팬더스 데이터프레임으로 읽기    ## ↱ 필드 구분 기호를 쉼표(sep=',')로 지정 // header=0 : 열 헤더를 파일 첫 행으로 지정
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)   ## pandas의 read_csv() 함수를 사용하여 CSV 파일을 읽어 데이터프레임에 넣는다.
wine.columns = wine.columns.str.replace(' ', '_')   ## 열 헤더에 포함되어 있는 공백을 밑줄로 바꾼다(fixed acidity -> fixed_acidity)
print(wine.head())  ## head() : 헤더 행과 처음 5개 행을 출력 -> () 안에 숫자를 넣으면, 그 숫자만큼 출력

# 변수별 요약통계 표시
print(wine.describe())  ## describe() : 수치형 변수들에 대한 요약통계를 출력
# ↳ 관측값 개수(count), 평균(mean), 표준편차(std), 최솟값(min)
#   25번째 백분위 수(25%), 중앙값(50%), 75번째 백분위 수(75%), 최댓값(max)

# 유일값 찾기
print(sorted(wine.quality.unique()))    ## quality.unique() : 유일값 출력

# 빈도 계산
print(wine.quality.value_counts())    ## quality.value_counts() : 유일값별 관측값 개수를 내림차순으로 정렬하여 출력