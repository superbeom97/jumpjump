### 3.2 단일 워크시트 처리 - 2 특정 행 필터링하기 - 특정 조건을 충족하는 행의 필터링 - 팬더스 코드
## 특정 단어나 숫자가 포함된 행의 하위 집합만 필요하거나 특정 날짜와 연관된 행의 하위 집합만 필요할 수 있다.
## 필요하지 않은 행은 걸러내고 필요한 행을 유지할 수 있다.
## Sale Amount 열의 데이터 값이 $1,400.00보다 큰 행을 선택

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
## data_frame의 이름 뒤에 []를 쓰고 선택하려는 열의 이름과 특정 조건을 지정하면
## 조건에 맞는 행을 쉽게 필터링할 수 있다.
## 여러 조건을 동시에 적용해야 하는 경우, 조건을 괄호 안에 넣고 적용할 조건부 논리에 딸 & 또는 |와 함께 쓴다.
## >> data_frame_value_meets_condition = data_frame[(data_frame['Sale Amount'].astype(float) > 1400.0) & (data_frame['Sale Amount'].astype(float) < 1800.0)]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()