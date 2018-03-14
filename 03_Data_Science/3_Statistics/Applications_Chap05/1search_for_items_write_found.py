### 5.1 대량의 파일에서 원하는 집합 찾기
## ↳ 대량의 기록 파일들로부터 특정 기록을 찾는 문제

## 기록 파일이 많은 경우에는 필요한 데이터를 찾기 어려울 수 있다. 예를 들어, 300개의 엑셀 파일과 200개의 CSV 파일
## 이 같은 경우, 파이썬 코딩 기술을 적용한다면, 전 과정을 자동화하여 시간을 절약하고 오류를 없앨 수 있다!
## ↳ 특정 품목 번호를 검색해 보자!

## 찾고자 하는 품목 번호를 튜플이나 리스트로 파이썬 스크립트에 직접 하드코딩할 수도 있지만
## 검색할 아이템의 수가 늘어날 경우, 수정이 어렵거나 실행이 불가능하게 된다.
## ↳ 따라서 입력 데이터를 스크립트로 전달하고, 이 CSV 입력 파일의 열에 나열된 품목 번호만 검색하도록 스크립트를 작성하자!!


import csv
import glob     ## 특정 패턴과 일치하는 모든 경로명을 찾는다 -> 폴더 내 다수 파일을 읽기 위해
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple     ## 파일에서 추출한 날짜들이 출력 파일에서 특정 포맷을 유지하도록

item_numbers_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]

## 찾으려는 품목 번호를 소스코드에서 사용하려면, CSV 파일에 있는 품목 번호를 리스트 같은 적합한 형태의 자료구조로 바꿔야 한다.
item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)  ## reader() : CSV 입력 파일을 연 후, 파일 내 데이터를 읽기 위해 filereader 객체를 만듦
    for row in filereader:
        item_numbers_to_find.append(row[0])
# print(item_numbers_to_find)

filewriter = csv.writer(open(output_file, 'a', newline=''))  ## writer() : 출력할 CSV 파일을 추가모드('a')로 열어서 데이터를 쓰기 위한 filewriter 객체를 만듦

file_counter = 0                ## 읽을 기록 파일의 수
line_counter = 0                ## 모든 파일에서 읽은 행의 수
count_of_item_numbers = 0       ## 찾고 있는 품목 번호가 들어 있는 행의 수
## 기록 파일 폴더 내에 있는 각 파일들을 반복 처리하기 위한 외부 for문     ↱ *.* : 모든 파일을 뜻함
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):  ## os.path.join() 함수는 폴더의 경로를
    file_counter += 1                                   ## glob.glob() 함수를 사용하여, 특정 패턴과 일치하는 모든 파일명과 결합
    if input_file.split('.')[1] == 'csv':   ## input_file : glob.glob() 함수가 찾은 파일 리스트의 개별 파일명
        with open(input_file, 'r', newline='') as csv_in_file:
            filereader = csv.reader(csv_in_file)
            header = next(filereader)   ## next() : 파일의 첫 행인 헤더 정보를 읽어 header 변수에 할당
            for row in filereader:  ## 헤더를 제외하고 남은 행들에 대한 데이터를 반복 처리하는 for문
                row_of_output = []
                for column in range(len(header)):
                    if column < 3:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)
                    elif column == 3:
                        cell_value = str(row[column]).lstrip('$').replace(',', '').split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)
                    # if column == 3:   위의 if, elif, else 구문을 이렇게 나누면 될 듯
                    #     cell_value = str(row[column]).lstrip('$').replace(',', '').split('.')[0].strip()
                    #     row_of_output.append(cell_value)
                    # else:
                    #     cell_value = str(row[column]).strip()
                    #     row_of_output.append(cell_value)
                row_of_output.append(os.path.basename(input_file))  ## os.path.basename() : 파일명 알아내기 -> 파일명을 추가
                if row[0] in item_numbers_to_find:  ## 행의 품목 번호가 찾으려는 품목 번호인지 아닌지 확인 -> 두 번째 for문 앞에 둬서, 일치하면 두 번째 for문을 수행하도록 하는 게 더 나을 듯
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers += 1
                line_counter += 1
    elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
        workbook = open_workbook(input_file)    ## open_workbook() : 엑셀 워크북을 열고 workbook 변수에 워크북의 내용을 할당
        for worksheet in workbook.sheets():   ## 워크북 내에 있는 워크시트들을 반복 처리
            try:
                header = worksheet.row_values(0)    ## 워크시트의 첫 번째 열인 헤더 행을 header 변수에 할당
            except IndexError:
                pass
            for row in range(1, worksheet.nrows):   ## 엑셀 파일의 남은 행들을 반복 처리 -> 헤더 행을 생략하고 두 번째 열부터 시작하기 위해 range 0 대신 1 에서부터 시작
                row_of_output = []
                for column in range(len(header)):
                    if column < 3:
                        cell_value = str(worksheet.cell_value(row, column)).strip()
                        row_of_output.append(cell_value)
                    elif column == 3:
                        ## Cost 열에서, 엑셀 파일에는 달러 기호가 포함되어 있지 않으므로(파일을 열어보면 포함되어 있는데..) CSV 파일을 읽을 때와는 달리 달러 기호를 제거하는 작업은 필요하지 않다.
                        cell_value = str(worksheet.cell_value(row, column)).split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                        cell_value = str(date(*cell_value[0:3])).strip()
                        row_of_output.append(cell_value)
                row_of_output.append(os.path.basename(input_file))      ## os.path.basename() : 파일명 알아내기 -> 엑셀 파일의 이름을 추가
                row_of_output.append(worksheet.name)                    ## 워크시트의 이름도 추가
                if str(worksheet.cell(row, 0).value).split('.')[0].strip() in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers += 1
                line_counter += 1
print('Number of files: {}'.format(file_counter))
print('Number of lines: {}'.format(line_counter))
print('Number of item numbers: {}'.format(count_of_item_numbers))