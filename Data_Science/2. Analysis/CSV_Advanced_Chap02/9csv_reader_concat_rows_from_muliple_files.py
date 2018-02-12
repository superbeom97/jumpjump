### 2.10 여러 파일의 데이터 합치기 - 기본 파이썬 코드
## 유사한 데이터가 들어 있는 여러 개의 파일이 있는 경우 모든 데이터가 하나의 파일에 포함되도록 데이터를 합쳐야 하는 경우가 있다.
## 앞 절에서 작성한 세 개의 CSV 파일을 사용하여 여러 개의 파일 속에 있는 데이터를 하나로 합치는 방법을 살펴보자
## -> 여라 입력 파일 속 데이터를 하나의 출력 파일로 수직으로 합쳐보자
## 'Run >> Edit Configurations'에서 'Script parameters'에
## -> "D:\Python_workspace\jumpjump\Data_Science\2. Analysis\CSV_Advanced_Chap02" output_files\\9output

# !/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader)
                for row in filereader:
                    filewriter.writerow(row)