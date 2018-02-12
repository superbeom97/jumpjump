### 2.11 파일에서 데이터 값의 합계 및 평균 계산하기 - 팬더스 코드
## 여러 개의 입력 파일이 있을 때 각 입력 파일에 대해 몇 가지 통계 수치를 계산
## 앞에서 만든 세 개의 CSV 파일을 사용하여, 각각의 입력 파일에서 열의 합계와 평균을 계산해볼 것이다

## 팬더스는 행 및 열의 통계 수치를 계산하는데 사용할 수 있는 sum 및 mean 같은 요약통계 함수를 제공

# !/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)

    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    average_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()

    data = {'file_name':os.path.basename(input_file), 'total_sales':total_sales, 'average_sales':average_sales}

    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)