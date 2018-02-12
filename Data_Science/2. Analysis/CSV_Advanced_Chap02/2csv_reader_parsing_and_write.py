### 2.4 CSV 파일 읽고 쓰기(파트2) - 기본 문자열 파싱이 실패하는 경우
### -> 마지막 두 행에 데이터 값 자체에 쉼표를 포함 - 1csv_read_with_simple_parsing_and_write.py 코드처럼 하면 파싱 실패
## => 파이썬에 내장된 csv 모듈을 임포트해서 $6,015.00과 $1,006,015.00이 포함된 입력 파일을 처리
## -> csv 모듈을 사용하는 법과 데이터 값에 포함되어 있는 쉼표를 처리하는 법을 배우게 될 것이다!

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')    ## filewriter 변수를 선언하고
        for row_list in filereader:
            filewriter.writerow(row_list)       ## writerow() -> 각 행의 값을 리스트 자료형으로 출력 파일에 써라