### Housing - Cost Function 구하기

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

housing_file_path = 'housing.csv'
housing = pd.read_csv(housing_file_path)        ## pandas의 read_csv() 함수를 사용하여 CSV 파일을 읽어 데이터프레임에 넣는다.
# print(housing.columns)
housing = housing.replace('yes', 1)
housing = housing.replace('no', 0)

housing_price_data = housing.price
# print(housing_price_data)

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while True:
    if i != 540:
        housing_price_datalist.append(housing_price_data[i])
        i += 1
    else:
        break

housing_predictors = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway', 'recroom',
                      'fullbase', 'gashw','airco', 'garagepl', 'prefarea']

x = housing[housing_predictors]
y = housing_price_data

housing_model = DecisionTreeRegressor()
housing_model.fit(x, y)

t = 0
while True:
    if t != 540:
        housing_price_predict_list.append(housing_model.predict(x.head())[t])     ## head() : 5개만 출력, head(20) 처럼 괄호 안에 숫자를 넣으면 그 갯수만큼 출력
        t += 1
    else:
        break

# print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
# c = list(map(lambda x,y: (x,y), A,B))
# print(c)

result_value = 0
for value in [x - y for x, y in zip(A, B)]:
    result_value += value ** 2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)

"""                  m
Cost Function = 1/m ∑ (선값(x) - 실제값(x))^2
                    i=1
"""
