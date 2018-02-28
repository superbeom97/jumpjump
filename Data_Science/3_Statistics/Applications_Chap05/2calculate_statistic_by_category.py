### 5.2 CSV 파일에서 카테고리별 통계치 계산하기

## 대부분의 비즈니스 분석은 특정 기간 특정 카테고리(개수는 미정)의 수치에 대한 통계치를 계산해야 한다.
## ↳ 카테고리 수가 미정일 때 통계치를 계산
## 비즈니스 분석을 하다 보면 입력 데이터의 행 사이의 차이를 계산해야 할 때가 많이 있다.
## 입력 파일 내 행 간 차이를 계산하고 다른 열을 기준으로 이 차이를 집계하는 방법을 살펴보자!


import csv
import sys
from datetime import date, datetime     ## date : 현재 날짜를 가져오기 위해 // datetime : 날짜 간 차이를 계산하기 위해

def date_diff(date1, date2):
    try:
        diff = str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y')).split()[0]
    except:
        diff = 0
    if diff == '0:00:00':   ## 두 날짜가 같아 그 차이가 0일 때, 따라서 값이 '0:00:00'이 될 때
        diff = 0
    return diff

input_file = sys.argv[1]
output_file = sys.argv[2]

packages = {}   ## 빈 딕셔너리
## 각 열에 해당하는 변수 3개
previous_name = 'N/A'
previous_package = 'N/A'
previous_package_date = 'N/A'
first_row = True    ## first_row 변수를 사용하여, 입력 파일의 첫 번째 행을 처리할 것이다
today = date.today().strftime('%m/%d/%Y')   ## 오늘의 날짜를 '%m/%d/%Y' 형식의 문자열로 today 변수에 저장
## print(today) >> 02/28/2018

with open(input_file, 'r', newline='') as input_csv_file:
    filereader = csv.reader(input_csv_file)
    header = next(filereader)
    for row in filereader:      ## 입력 파일의 헤더를 제외한 남은 행들을 반복 처리
        current_name = row[0]
        current_package = row[1]
        current_package_date = row[3]
        if current_name not in packages:    ## current_name의 값이 packages 딕셔너리에 포함되어 있지 않다면,
            packages[current_name] = {}     ## packages 딕셔너리에 current_name의 값을 키로 저장 - 키에 해당하는 값은 빈 딕셔너리로 지정
        if current_package not in packages[current_name]:   ## current_package의 값이 내부 딕셔너리 packages[current_name]에 포함되어 있지 않다면,
            packages[current_name][current_package] = 0     ## 내부 딕셔너리 packages[current_name]에 current_package의 값을 키로 저장 - 키에 해당하는 값은 정수 0으로 지정
        if current_name != previous_name:   ## 현재 이름과 이전 이름이 동일하지 않은지 확인
            if first_row:
                first_row = False
            else:
                diff = date_diff(today, previous_package_date)
                if previous_package not in packages[previous_name]:
                    packages[previous_name][previous_package] = int(diff)
                else:
                    packages[previous_name][previous_package] += int(diff)
        else:
            diff = date_diff(current_package_date, previous_package_date)
            packages[previous_name][previous_package] += int(diff)      ## 예) {'John Smith':{'Silver':0,'Bronze':52}}
        previous_name = current_name            ## 현재 행의 데이터가 이전 행의 데이터가 된다.
        previous_package = current_package
        previous_package_date = current_package_date

header = ['Customer Name', 'Category', 'Total Time (in Days)']
with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header)
    for customer_name, customer_name_value in packages.items():
        for package_category, package_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, package_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(package_category_value)
            filewriter.writerow(row_of_output)