### 2.5.2 특정 집합의 값을 포함하는 행의 필터링 - 팬더스 코드
## Purchase Date 열의 구매 일자가 집합 {'1/20/14', '1/30/14'}를 포함하는 경우, 해당 행을 찾아서 출력 파일에 쓴다

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)