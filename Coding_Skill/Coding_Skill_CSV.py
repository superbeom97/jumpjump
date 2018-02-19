import glob     ## glob 모듈 : 특정 패턴과 일치하는 모든 경로명을 찾는다

################################## 1. startswith() : 어떤 문자로 시작하는지 체크!! ##################################
### startswith() 함수를 사용하여 정규 표현식을 사용하지 않고, 데이터를 검색(정규 표현식 대신 사용 가능)
## 문자열 데이터 타입에 대해, 대상 문자열이 어떤 문자로 시작하는지를 체크

## 정규 표현식 : pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.IGNORECASE)
## startswith() : data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number'].str.startswith("001-"), :]
## ↳ Data_Science - 2.Analysis - CSV_Advanced_Chap02 - 5pandas_value_matches_pattern.py

print('[Absolutely]'.startswith('A'))
## >> False
print('[Absolutely]'.startswith('['))
## >> True
print('[Absolutely]'.startswith('[Abso'))
## >> True


################################## 2. 경로에 있는 여러 파일 불러오기 ##################################
## for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
## => input_path 경로에 있는 'sales_*'가 포함된 파일을 하나의 리스트로 만들어라!!
## ↳ Data_Science - 2.Analysis - CSV_Advanced_Chap02 - 8csv_reader_counts_for_multiple_files.py

### 2.9 여러 개의 CSV 파일 읽기 - 2.9.1 전체 파일 개수 및 각 파일의 행 및 열 개수 계산 - 기본 파이썬 코드
## 파이썬의 내장된 glob 모듈을 소개하고, 앞서 소개한 예제들을 토대로 여러 개의 CSV 파일을 처리하는 방법을 알아보자
## -> 행과 열의 개수를 세어보는 간단한 일부터 시작해보자
## 'Run >> Edit Configurations'에서 'Script parameters'에 'sales_*' 파일이 있는 경로를 " " 안에 입력
## -> "D:\Python_workspace\jumpjump\Data_Science\2.Analysis\CSV_Advanced_Chap02"

# !/usr/bin/env python3
import csv
import glob     ## glob 모듈 : 특정 패턴과 일치하는 모든 경로명을 찾는다
import os       ## os 모듈 : 경로명을 파싱하는 데 유용한 함수를 포함
import sys

input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):   ## glob.glob()과 os.path.join()은 세 개의 입력 파일이 들어 있는 리스트를 만듦
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Number of files: {0:d}'.format(file_counter))


## os.path.basename(path)는 입력받은 경로에서 파일명을 반환한다.
## path가 "C:\User\Clinton\Desktop\my_input_file.csv"라면 os.path.basename(path)는 my_input_file.csv를 반환한다.
## 전체 경로명의 마지막 요소를 추출

## for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
## os.path.join() : 괄호 안에 있는 두개의 컴포넌트를 결합
##  - input_path : 입력 파일이 들어 있는 폴더의 경로
##  - sales_* : sales_ 패턴으로 시작하는 파일의 이름
## glob 모듈의 glob.glob() : sales_*의 '*'를 실제 파일명으로 확장
## glob.glob()과 os.path.join()은 세 개의 입력 파일이 들어 있는 리스트를 만든다
## => input_path 경로에 있는 'sales_*'가 포함된 파일을 하나의 리스트로 만들어라!!