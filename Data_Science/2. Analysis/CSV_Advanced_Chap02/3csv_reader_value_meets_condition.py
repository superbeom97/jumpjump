### 2.5 특정 행을 필터링하기 - 1 특정 조건을 충족하는 행의 필터링 - 기본 파이썬 코드
## -> 'Supplier Name'이 'Supplier Z'이거나 또는 'Cost'가 '$600.00' 이상인 행만 필터링

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            cost = str(row_list[3]).strip('$').replace(',', '')
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row_list)