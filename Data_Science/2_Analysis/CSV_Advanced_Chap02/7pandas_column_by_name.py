### 2.6 특정 열 선택하기 - 2.6.2 열의 헤더를 사용하여 특정 열을 선택하는 방법 - 팬더스 코드
## 이 방법은 포함하려는 열 헤더를 식별하기 쉽거나,
## 여러 개의 입력 파일을 처리할 때 열의 헤더는 같지만 열의 위치가 입력 파일에 따라 다를 때 효과적
## -> Invoice Number 및 Purchase Date 열만 포함해 보자

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
## 4pandas_value_in_set.py과 마찬가지로 loc를 사용하여 간단하게 나타낸

data_frame_column_by_name.to_csv(output_file, index=False)