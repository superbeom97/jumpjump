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
print("")
print("<< 그룹별 기술통계 구하기 >>\n".center(60))                                                                    ## count : 개수, mean : 평균, std : 표준편차
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))


##################################### 변수별로 서로 다른 통계량 구하기
print("")
print("<< 변수별로 서로 다른 통계량 구하기 >>\n".center(60))
print(churn.groupby(['churn']).agg({'day_charge' : ['mean', 'std'],     ## mean : 평균, std : 표준편차
                                    'eve_charge' : ['mean', 'std'],
                                    'night_charge' : ['mean', 'std'],
                                    'intl_charge' : ['mean', 'std'],
                                    'account_length' : ['count', 'min', 'max'],         ## count : 개수, min : 최솟값, max : 최댓값
                                    'custserv_calls' : ['count', 'min', 'max']}))


##################################### 새로운 변수 total_charges를 기준으로 그룹화한 뒤,
##################################### ★ 그룹별 통계량 구하기 ★
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
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])      ## qcut() : 정수 또는 사분위수를 담은 배열을 인수로 취한다.
# factor_qcut = pd.qcut(churn.account_length, 4)                            ## 따라서 [0., 0.25, 0.5, 0.75, 1.] 대신 정수 4를 사용하여 사분위수 지정도 가능
# factor_qcut = pd.qcut(churn.account_length, 10)   ## 정수 10을 사용하여 십분위수를 지정할 수도 있다.
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())


##################################### intl_plan 와 vmail_plan 열에 대한 이진형 지시변수를 만들고,
##################################### churn 열과 병합하여 새로운 데이터프레임을 생성하기
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')       ## prefix : 접두사로 붙임
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])   ## join() : churn 열과 새로운 이진형 지시변수를 병합
print(churn_with_dummies.head())


# ##################################### total_charges를 사분위수로 분할하고, 이진형 지시변수를 만들고,
# ##################################### 새로운 더미변수를 churn 데이터프레임에 추가하기
# qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
# total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
# dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
# churn_with_dummies = churn.join(dummies)
# print(churn_with_dummies.head())
#
#
# ##################################### 피벗 테이블 생성하기
# print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
# print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
# print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))