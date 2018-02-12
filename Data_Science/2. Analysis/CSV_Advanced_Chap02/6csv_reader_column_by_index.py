### 2.6 특정 열 선택하기 - 2.6.1 열의 인덱스 값을 사용하여 특정 열을 선택하는 방법 - 기본 파이썬 코드
## 이 방법은 열의 인덱스 값을 쉽게 식별할 수 있거나 여러 개의 입력 파일을 처리할 때,
## 또는 모든 입력 파일에서 열의 위치가 변경 되지 않는 경우에 효과적
## -> Supplier Name 및 Cost 열만 포함해 보자

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)