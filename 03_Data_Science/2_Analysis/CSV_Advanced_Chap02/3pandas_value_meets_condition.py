### 2.5 특정 행을 필터링하기 - 1 특정 조건을 충족하는 행의 필터링 - 팬더스 코드
## 'Supplier Name'이 'Supplier Z'이거나 또는 'Cost'가 '$600.00' 이상인 행만 필터링

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)