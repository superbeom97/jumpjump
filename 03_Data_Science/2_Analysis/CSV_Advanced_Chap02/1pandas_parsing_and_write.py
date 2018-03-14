### 2.2 CSV 파일 읽고 쓰기(파트1) - 2 팬더스 코드
## CSV 파일을 읽어서 다른 파일에 그대로 똑같이 쓰기

# !/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)    ## CSV 파일을 읽어 와 data_frame 변수에 할당
print(data_frame)
data_frame.to_csv(output_file, index=False)     ## data_frame에 할당된 CSV 파일을 쓰는 코드