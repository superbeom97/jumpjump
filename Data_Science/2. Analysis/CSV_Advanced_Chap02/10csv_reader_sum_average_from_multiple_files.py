### 2.11 파일에서 데이터 값의 합계 및 평균 계산하기 - 기본 파이썬 코드
## 여러 개의 입력 파일이 있을 때 각 입력 파일에 대해 몇 가지 통계 수치를 계산
## 앞에서 만든 세 개의 CSV 파일을 사용하여, 각각의 입력 파일에서 열의 합계와 평균을 계산해볼 것이다

# !/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1.0
        average_sales = '{0:2f}'.format(total_sales / number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()