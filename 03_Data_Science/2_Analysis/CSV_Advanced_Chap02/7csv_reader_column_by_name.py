### 2.6 특정 열 선택하기 - 2.6.2 열의 헤더를 사용하여 특정 열을 선택하는 방법 - 기본 파이썬 코드
## 이 방법은 포함하려는 열 헤더를 식별하기 쉽거나,
## 여러 개의 입력 파일을 처리할 때 열의 헤더는 같지만 열의 위치가 입력 파일에 따라 다를 때 효과적
## -> Invoice Number 및 Purchase Date 열만 포함해 보자
## => '열 헤더'에서 해당 '인덱스'를 뽑아내서 2.6.1 방법을 사용하는

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)