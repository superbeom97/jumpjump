### 2.7 연속된 행 선택하기 - 기본 파이썬 코드
## 때론 분석해야 하는 파일 맨 위 또는 맨 아래에 처리할 필요가 없는 애용이 포함되어 있다.
## 예를 들어 파일의 맨 위에 문서 제목과 작성자를 쓴 행이 있거나 파일의 맨 아래에 출처, 주의사항, 메모 등이 있는 경우
## -> 파일의 맨 위, 열 헤더가 있는 행 위에 세 개 행을 삽입 - I don't care about this line 식으로 필요 없는 텍스트 추가
## 맨 아래, 즉 마지막 데이터 행 아래 세 행에도 마찬가지로 필요 없는 덱스트 추가 - I don't want this line either

# !/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter = 0     ## 특정 행을 선택하기 위해 row_counter 변수 추가 -> 행 번호 추적 -> 포함할 행을 식별하고 선택 가능
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1