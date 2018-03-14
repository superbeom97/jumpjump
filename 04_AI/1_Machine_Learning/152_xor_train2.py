import pandas as pd
from sklearn import svm, metrics

## XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

## 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:1]     ## 데이터
xor_label = xor_df.ix[:,2]      ## 레이블

## 데이터 학습과 예측하기 --- (※2)
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

## 정답률 구하기 --- (※3)
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)


### 파이썬과 pandas의 슬라이싱은 다르다.
## xor_data = xor_df.ix[:,0:2]
## 파이썬에서는 슬라이싱할 때, 끝에 값은 포함이 안 되는데 -> 0, 1만 선택
## 판다스에서는 포함합니다! -> 0 ~ 2(0, 1, 2)까지 선택

### DataFrame.ix[rows, columns] : 축의 라벨을 사용해서 데이터프레임의 행과 열을 선택할 수 있음
## data.ix[1:2, 'age']  : data 1번, 2번 행에서 age만 꺼내옴
## df.ix[val] : 데이터프레임에서 행의 부분집합을 선택
## df.ix[:, val] : 데이터프레임에서 열의 부분집합을 선택
