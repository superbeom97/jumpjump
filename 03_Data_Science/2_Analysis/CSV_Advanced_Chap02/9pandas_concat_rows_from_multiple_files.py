### 2.10 여러 파일의 데이터 합치기 - 팬더스 코드
## 유사한 데이터가 들어 있는 여러 개의 파일이 있는 경우 모든 데이터가 하나의 파일에 포함되도록 데이터를 합쳐야 하는 경우가 있다.
## 앞 절에서 작성한 세 개의 CSV 파일을 사용하여 여러 개의 파일 속에 있는 데이터를 하나로 합치는 방법을 살펴보자
## -> 여라 입력 파일 속 데이터를 하나의 출력 파일로 수직으로 합쳐보자
## 'Run >> Edit Configurations'에서 'Script parameters'에
## -> "D:\Python_workspace\jumpjump\03_Data_Science\2_Analysis\CSV_Advanced_Chap02" output_files\\9output

## (팬더스) 기본 프로세스는 각 입력 파일을 데이터프레임으로 읽어 들이고 all_data_frame 리스트에 추가한 다음
## concat() 함수를 사용하여 모든 데이터프레임을 하나의 데이터프레임으로 합친다.
## concat() 함수는 axis 인수를 통해서 데이터프레임을 병합하는 방향을 수직(axis=0) 또는 수평(axis=1)으로 지정할 수 있다.

# !/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)