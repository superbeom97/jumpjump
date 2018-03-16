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
print("\nCoefficients:\n%s" % logit_model.params)               ## 로지스틱 회구모형의 계수들
print("\ntotal_charges's coefficient:\n%s" % logit_model.params[3])                ## 인덱스 또는 이름을 이용하여 개별 회귀계수를 추출할 수 있다.
print("\ntotal_charges's coefficient:\n%s" % logit_model.params['total_charges'])
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)        ## 계수 표준편차들 오류 ??


##################################### 2 회귀계수 해석
### 로지스틱 회귀는 S자 곡선이므로 독립변수가 한 단위만큼 변할 때, 기대되는 종속변수의 변화가 일정하지 않다.
### 회귀계수가 종속변수의 성공 확률에 미치는 영향을 파악하기 위해서는 모형 평가의 기준, 즉 오즈(odds)가 필요
### 기준 오즈는 모든 독립변수가 0인 경우에 성공 확률에 미치는 영향을 나타낸다.
### 기준 오즈 값은 그 자체로서는 그다지 의미가 없으므로, 먼저 모든 독립변수를 평균으로 설정하여 모형을 평가해야 한다.

## 이러한 ★ 로짓 함수의 역함수를 ★ 로지스틱 함수라고 부른다.
## 특히, 이러한 함수의 형태를 ★ 시그모이드(sigmoid) 함수라고 한다.
def inverse_logit(model_formula):                   ## 선형회귀모형의 연속형 예측값을 0과 1 사이의 확률로 변환하는 함수
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula)))
    # return (1.0 / (1.0 + np.exp(-model_formula)))     ## numpy를 임포트 했다면 굳이 exp를 임포트 할 필요 없음
                                                        ## numpy 안에 exp 함수가 포함되어 있다.

## 모든 독립변수를 평균으로 설정했을 때의 예측값을 추정
at_means = float(logit_model.params[0]) + \
           float(logit_model.params[1])*float(churn['account_length'].mean()) + \
           float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
           float(logit_model.params[3])*float(churn['total_charges'].mean())
## logit_model.params[0] = const              ↳ 해당 열(독립변수)의 계수에, 해당 열(독립변수)의 평균을 곱해서 더하는 건가?
## logit_model.params[1] = account_length     로지스틱 회귀모형의 계수들
## logit_model.params[2] = custserv_calls
## logit_model.params[3] = total_charges
## churn['account_length'].mean() : 독립변수들의 평균(이 라인은 'account_length'의 평균)

print("churn['account_length'].mean() : ", churn['account_length'].mean())
print("churn['custserv_calls'].mean() : ", churn['custserv_calls'].mean())
print("churn['total_charges'].mean() : ", churn['total_charges'].mean())
print("at_means : ", at_means)

## at_means 값을 로지스틱 함수에 입력했을 때 출력되는 결과를 소수점 세 자리로 출력
print("P of churn when ind. vars are their mean: %.3f" % inverse_logit(at_means))
## -> -2.068(at_means)의 로짓 역함수를 취하면 0.112(inverse_logit(at_means))이고,
##   따라서 "이탈 고객 사이"에서 "account_length, custserv_call, total_charges의 평균이 똑같을 확률"은 "11.2%" 라고 말할 수 있다.


## 독립변수 중 "하나의 단위 변화에 대한 종속변수의 변화를 평가"하려면,
## 독립변수 중 하나를 "평균에 가까운 값"으로 변경하여 확률의 차이를 평가할 수 있다.
## 예를 들어, custserv_calls 열을 기준으로 살펴보자.
cust_serv_mean = float(logit_model.params[0]) + \
                 float(logit_model.params[1])*float(churn['account_length'].mean()) + \
                 float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
                 float(logit_model.params[3])*float(churn['total_charges'].mean())

## custserv_calls의 평균에서 1을 빼라
## (고객 서비스 호출 한 단위 증가시키려면 +1이 아닌, -1이구나!! 아니면 그냥 평균에 가까운 값으로 변경하려고 -1을 한 건가??)
cust_serv_mean_minus_one = float(logit_model.params[0]) + \
                           float(logit_model.params[1])*float(churn['account_length'].mean()) + \
                           float(logit_model.params[2])*float(churn['custserv_calls'].mean()-1.0) + \
                           float(logit_model.params[3])*float(churn['total_charges'].mean())

print("cust_serv_mean : ", cust_serv_mean)
print("churn['custserv_calls'].mean()-1.0 : ", churn['custserv_calls'].mean()-1.0)
print("cust_serv_mean_minus_one : ", cust_serv_mean_minus_one)

## 둘 모두 로지스틱 함수를 취하여 cust_serv_mean의 추정값에서 cust_serv_means_minus_one의 추정값을 뺀다.
print("Probability of churn when account length changes by 1: %.3f" % (inverse_logit(cust_serv_mean) - inverse_logit(cust_serv_mean_minus_one)))
## ↳ 0.037이 나온다. -> "custserv_calls의 평균 근처"에서 "고객 서비스 호출이 한 단위 증가"하는 경우,
##                     "이탈 확률이 3.72% 증가"한다고 말할 수 있다.


##################################### 3 예측하기 - 음...?
### 선형회귀 예측과 마찬가지로, 로지스틱 회귀모형을 사용하여 '새로운' 관측값에 대해 예측할 수 있다.

## 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
new_observations = churn.ix[churn.index.isin(range(10)), independent_variables.columns]
## ix[행축 번호, 열축번호] : 축 라벨을 사용해서 데이터프레임의 행과 열을 선택할 수 있다.

new_observations_with_constant = sm.add_constant(new_observations, prepend=True)    ## statsmodels의 add_constant() : 입력변수에 전체 값이 1인 열을 추가

y_predicted = logit_model.predict(new_observations_with_constant)   ## 로지스틱 회귀모형으로 예측한 10개의 값을 y_predicted에 할당
y_predicted_rounded = [round(score, 2) for score in y_predicted]    ## round(A, B) - A : 적용할 숫자, B : 반올림해서 표현할 자릿수
                                                        ## round(score, 2) : score를 반올림해서 소수점 둘째 자리까지 표현해라
                                                        ## round(score) : score를 반올림해서 정수로 표현해라
print(y_predicted_rounded)