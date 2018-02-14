### 2.8 헤더 추가하기 - 기본 파이썬 코드
## 때로는 스프레드시트에 헤어 행이 포함되지 않는 경우가 종종 있다
## 이런 경우에 파이썬 스크립트를 이용해 열 헤더를 추가할 수 있다

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']   ## 각 열의 헤더들이 들어 있는 리스트 변수를 만듦
        filewriter.writerow(header_list)    ## 각 열의 헤더들이 들어 있는, 리스트의 값을 출력 파일의 첫 번째 행에 씀
        for row in filereader:          ## 헤더 행 이후의 모든 데이터 값을 출력 파일에 씀
            filewriter.writerow(row)