import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

# 데이터셋을 데이터프레임으로 읽음
iris = pd.read_csv('iris.csv', sep=',', header=0)
iris.columns = [heading.lower() for heading in iris.columns.str.replace('.','_')]

iris['YesorNo'] = np.where(iris['variety'] == 'Setosa', 1., 0.)


## 1 로지스틱 회귀분석
dependent_variable = iris['YesorNo']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)


## 3 예측하기
# 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
# sample_index_list=[2,5,7,9,40,55,78,99,101,102]
# new_observations = iris.ix[iris.index.isin(sample_index_list), independent_variables.columns]
new_observations = iris.ix[iris.index.isin(range(150)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)