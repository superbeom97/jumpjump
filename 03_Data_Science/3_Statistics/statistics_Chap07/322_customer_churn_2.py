## 통신사의 현재 고객과 이탈 고객에 해당하는 3,333개 관측값이 포함되어 있다.
## 20개의 입력 변수와 1개의 출력 변수로 구성
## 출력 변수는 고객 이탈 여부를 나타내는 이진 변수로서 데이터 수집 시점에서 고객의 이탈 여부를 나타낸다.
## 입력 변수는 고객의 요금제 특성과 통화 습관 등이 기록되어 있다.

#### 7.3 고객 이탈 데이터셋

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


##################################### 데이터셋을 데이터프레임으로 읽음
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ','_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)    ## np.where(X, arr, brr) : X가 True 이면 arr, False 이면 brr
print("<< churn.head() >>\n".center(60))
print(churn.head())     ## head() : 5개만 출력, head(20) 처럼 괄호 안에 숫자를 넣으면 그 갯수만큼 출력
# print(churn.head(20))


##################################### 그룹별 기술통계 구하기
## 데이터프레임을 만들었으므로 전체 데이터를 유지 고객와 이탈 고객으로 그룹화해서 기술통계를 구할 수 있다.
## 이를 통해 두 고객 그룹 사이의 차이점을 찾아낼 수 있는지 알아보자.

## """churn 열의 값을 기준으로""" 전체 데이터를 유지 고객과 이탈 고객으로 그룹화한다. - groupby : 설정한 column에 대해서 그룹별로 묶어주는 작업
## 그 다음, 그룹별로 6개의 열에 대해 세 가지 통계량(개수, 평균, 표준편차)을 산출한다. - agg(aggregate) : 사용하여 그룹별로 집계를 위한 작업을 해줘야 함
print("\n")
print("<< 그룹별 기술통계 구하기 >>\n".center(60))                                                                    ## count : 개수, mean : 평균, std : 표준편차
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))


##################################### 변수별로 서로 다른 통계량 구하기
print("\n")
print("<< 변수별로 서로 다른 통계량 구하기 >>\n".center(60))
print(churn.groupby(['churn']).agg({'day_charge' : ['mean', 'std'],     ## mean : 평균, std : 표준편차
                                    'eve_charge' : ['mean', 'std'],
                                    'night_charge' : ['mean', 'std'],
                                    'intl_charge' : ['mean', 'std'],
                                    'account_length' : ['count', 'min', 'max'],         ## count : 개수, min : 최솟값, max : 최댓값
                                    'custserv_calls' : ['count', 'min', 'max']}))


##################################### 새로운 변수 total_charges를 기준으로 그룹화한 뒤,
##################################### ★ 그룹별 통계량 구하기 ★
print("\n")
print("<< total_charges를 기준으로 그룹화한 뒤, 그룹별 통계량 구하기 >>\n".center(60))

## day_charge, eve_charge, night_charge, intl_charge 열의 데이터를 합산하여 새로운 변수 total_charges를 만든다.
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']
## cut(X, 5, precision=2) -- cut(X) : X 변수의 데이터를 나눈다 // 5 : """폭이 같은""" 5개의 구간으로 // precision=2 : 소수점 둘째자리까지
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
# print(factor_cut)
def get_stats(group):
    return {'min':group.min(), 'max':group.max(), 'count':group.count(), 'mean':group.mean(), 'std':group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())     ## unstack() : 가로로 출력 -> 가독성이 훨씬 올라간다!
# print(grouped.apply(get_stats))     ## unstack()이 없으면 세로로 출력

### apply()
## apply(함수, (인자or인자값들)) : 함수 간접 실행 - 함수 이름과 그 함수의 인자를 입력 받아, 간접적으로 함수를 실행


##################################### account_length 열의 """사분위수"""를 기준(관측값의 """개수"""를 거의 동일하게)으로 분할한 뒤,
##################################### ★ 그룹별 통계량 구하기 ★
print("\n")
print("<< account_length 열의 사분위수를 기준으로 분할한 뒤, 그룹별 통계량 구하기 >>\n".center(60))

factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])      ## qcut() : 정수 또는 사분위수를 담은 배열을 인수로 취한다.
# factor_qcut = pd.qcut(churn.account_length, 4)                            ## 따라서 [0., 0.25, 0.5, 0.75, 1.] 대신 정수 4를 사용하여 사분위수 지정도 가능
# factor_qcut = pd.qcut(churn.account_length, 10)   ## 정수 10을 사용하여 십분위수를 지정할 수도 있다.
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())


##################################### intl_plan 와 vmail_plan 열에 대한 이진형 지시변수를 만들고,
##################################### churn 열과 병합하여 새로운 데이터프레임을 생성하기
print("\n")
print("<< intl_plan/vmail_plan -> 이진형 지시변수 -> churn 열과 병합 >>\n".center(60))

intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')       ## prefix : 접두사로 붙임
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
## get_dummies(A) : 이진형 지시변수를 만듦 - A가 있으면 1, 없으면 0
## intl_plan과 vmail_plan의 경우 값이 yes와 no, 두 가지가 있다 -> 각각에 대해 두 개의 열을 만들어 준다.
## 'intl_plan_no'에선 no가 있으면 1, yes가 있으면 0 // 'intl_plan_yes'에선 yes가 있으면 1, no가 있으면 0

churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])   ## join() : churn 열과 새로운 이진형 지시변수를 병합
print(churn_with_dummies.head())


##################################### total_charges를 사분위수로 분할하고, 이진형 지시변수를 만들고,
##################################### 새로운 더미변수를 churn 데이터프레임에 추가하기
print("\n")
print("<< total_charges 사분위수로 분할 - 이진형 지시변수 - churn 데이터프레임에 추가 >>\n".center(60))

qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)    ##  total_charges 열을 사분위수를 기준으로 분할하고,
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')       ##  labels : 분할된 각 사분위수에 qcut_name에서 지정한 이름을 붙인다.
## total_charge의 경우, intl_plan과 vmail_plan과 다르게 하나의 값만 있다 -> 각각에 대해 하나의 열만 만들어 준다.

churn_with_dummies = churn.join(dummies)    ## join() : 이 4개의 변수를 churn 데이터프레임에 추가
print(churn_with_dummies.head())    ## 각각의 데이터들이 들어 있는 사분위수에 1이 찍힘 - 이해가 안 되면 밑의 세 코드를 실행해 볼 것!

# factor_qcut = pd.qcut(churn.total_charges, 4)      ## qcut() : 정수 또는 사분위수를 담은 배열을 인수로 취한다.
# grouped = churn.custserv_calls.groupby(factor_qcut)
# print(grouped.apply(get_stats).unstack())


##################################### 피벗 테이블 생성하기 - ???
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))


##################################### ★★★ 1 로지스틱 회귀분석 ★★★
### 고객 이탈 데이터셋의 종속변수는 이진형으로서 고객의 이탈 여부를 나타낸다.
### 이처럼 종속변수의 값이 0과 1인 경우에는 선형회귀분석이 적합하지 않다.
### 선형회귀분석에서는 예측값이 0보다 작거나 1보다 클 수 있지만, 이는 확률에서 말이 안 되기 때문이다.
### 따라서 종속변수가 이진형이면 예측값을 0과 1 사이로 제한하는 로지스틱 회귀를 적용한다!!
### ↳ 로지스틱 회귀분석은 종속변수를 직접 모델링하지 않고, 종속변수가 특정 범주에 속하는 확률을 모델링한다!
### -> 로지스틱 회귀분석은 이진형 종속변수와 독립변수 간의 관계를 로지스틱 함수를 이용하여 추정한다.
###    이 함수는 연속형인 값을 입력 받아, 0과 1 사이의 값으로 변환한다. 이 예측값이 확률 값을 나타낸다.

## 선형회귀분석 구문과 달리, 로지스틱 회귀분석에서는 회귀식 대신, 독립변수와 종속변수를 따로 할당한다.
dependent_variable = churn['churn01']   ## churn01 열의 값들을 dependent_variable라는 새로운 변수에 할당
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]    ## 독립변수로 사용할 3개의 열을 지정, independent_variables에 할당
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)  ## statsmodels의 add_constant() : 입력변수에 전체 값이 1인 열을 추가
## ↳ prepend=True : 전체 값이 1인 const 열을 가장 처음(1열)에 배치 // prepend=False : 전체 값이 1인 const 열을 가장 마지막 열에 배치

## 로지스틱 회귀모형에 피팅하고, 그 결과를 logit_model 변수에 할당
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

### 해석 ???
print(logit_model.summary)
print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))   ## logit_model에서 추출할 수 있는 모든 통계량을 리스트 형태로 출력
print("\nCoefficients:\n%s" % logit_model.params)                   ## 계수들 ??
print("\ntotal_charges's coefficient:\n%s" % logit_model.params[3])                ## 인덱스 또는 이름을 이용하여 개별 회귀계수를 추출할 수 있다.
print("\ntotal_charges's coefficient:\n%s" % logit_model.params['total_charges'])
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)          ## 계수 표준편차들 오류 ??
