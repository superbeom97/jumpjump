### 2.5 특정 행을 필터링하기 - 2 특정 집합의 값을 포함하는 행의 필터링 - 기본 파이썬 코드
## -> Purchase Date 열의 구매 일자가 집합 {'1/20/14', '1/30/14'}를 포함하는 경우, 해당 행을 찾아서 출력 파일에 쓴다

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)