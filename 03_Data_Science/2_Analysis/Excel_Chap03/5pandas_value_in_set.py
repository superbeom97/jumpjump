### 3.2 단일 워크시트 처리 - 2 특정 행 필터링하기 - 특정 집합의 값을 포함하는 행의 필터링 - 팬더스 코드
## Purchase Date 열의 값이 특정 집합(01/24/2013 및 01/31/2013)에 포함되는 행을 필터링

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

important_dates = ['01/24/2013', '01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)] ## isin() : 특정 값이 리스트에 있는지 확인

writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()