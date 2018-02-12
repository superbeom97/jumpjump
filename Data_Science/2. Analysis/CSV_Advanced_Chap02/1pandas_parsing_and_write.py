### 2.2 CSV 파일 읽고 쓰기(파트1) - 2 팬더스 코드

# !/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)