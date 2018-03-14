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
        header = next(filereader)       ## ☆ next() -> 입력 파일의 첫 번째 행(헤더 행)을 header라는 리스트 변수로 할당
        filewriter.writerow(header)     ## 그 헤더 행을 출력 파일에 써라
        for row_list in filereader:
            supplier = str(row_list[0]).strip()  ## 각 행의 Supplier Name 열에 해당하는 값을 가져와서 supplier라는 변수에 할당
            cost = str(row_list[3]).strip('$').replace(',', '')     ## ☆ strip('$') -> 문자열에 포함된 '$' 제거
            if supplier == 'Supplier Z' or float(cost) > 600.0:     ## replace(',', '') -> 문자열에 포함된 ',' 제거
                filewriter.writerow(row_list)