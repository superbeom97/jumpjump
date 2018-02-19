### 3.2 단일 워크시트 처리 - 2 특정 행 필터링하기 - 특정 조건을 충족하는 행의 필터링 - 기본 파이썬 코드
## 특정 단어나 숫자가 포함된 행의 하위 집합만 필요하거나 특정 날짜와 연관된 행의 하위 집합만 필요할 수 있다.
## 필요하지 않은 행은 걸러내고 필요한 행을 유지할 수 있다.
## Sale Amount 열의 데이터 값이 $1,400.00보다 큰 행을 선택

# !/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []   ## 출력 파일에 쓰고자 하는 입력 파일의 모든 행을 이 리스트에 채울 것이다.
    header = worksheet.row_values(0)    ## 헤더 행 추출
    data.append(header)     ## 헤더 행을 있는 그대로 data에 추가
    for row_index in range(1, worksheet.nrows):
        row_list = []
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)     ## Sale Amount 열의 데이터 값을 담음
        if sale_amount > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)   ## 연속하는 행의 인덱스 값을 새로 얻기 위해서
            ## 이렇게 하지 않으면, xlwt의 write() 함수는 입력 파일의 기존 행 인덱스 값을 사용 -> 행 사이에 간격을 두고 출력 파일에 행을 쓴다.

    for list_index, output_list in enumerate(data):     ## enumerate() : 인덱스와 값을 분리시켜 줌
        ## 0  ['Customer ID', 'Customer Name', 'Invoice Number', 'Sale Amount', 'Purchase Date']
        ## 1  [2345.0, 'Mary Harrison', '100-0003', 1425.0, '01/06/2013']
        for element_index, element in enumerate(output_list):
            ## 0  Customer ID
            ## 1  Customer Name
            ## 2  Invoice Number
            ## 3  Sale Amount
            ## 4  Purchase Date
            output_worksheet.write(list_index, element_index, element)  ## 0, 0 자리에 Customer ID를 써라

output_workbook.save(output_file)