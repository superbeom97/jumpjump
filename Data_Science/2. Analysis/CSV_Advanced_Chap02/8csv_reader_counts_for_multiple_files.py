### 2.9 여러 개의 CSV 파일 읽기 - 2.9.1 전체 파일 개수 및 각 파일의 행 및 열 개수 계산 - 기본 파이썬 코드
## 파이썬의 내장된 glob 모듈을 소개하고, 앞서 소개한 예제들을 토대로 여러 개의 CSV 파일을 처리하는 방법을 알아보자
## -> 행과 열의 개수를 세어보는 간단한 일부터 시작해보자
## 'Run >> Edit Configurations'에서 'Script parameters'에 'sales_*' 파일이 있는 경로를 " " 안에 입력
## -> "D:\Python_workspace\jumpjump\Data_Science\2. Analysis\CSV_Advanced_Chap02"

# !/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} orws \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Number of files: {0:d}'.format(file_counter))