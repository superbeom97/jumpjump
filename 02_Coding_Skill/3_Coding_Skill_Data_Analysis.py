import pandas as pd
import numpy as np

################################## 1. np.where(X, arr, brr) & .head() ##################################
churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ','_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)    ## np.where(X, arr, brr) : X가 True 이면 arr, False 이면 brr
print(churn.head())     ## head() : 5개만 출력, head(20) 처럼 괄호 안에 숫자를 넣으면 그 갯수만큼 출력
# print(churn.head(20))


################################## 2. 하나의 열의 값을 기준으로 그룹별 기술통계 구하기 ##################################
## -> 317_customer_churn 코드 참고