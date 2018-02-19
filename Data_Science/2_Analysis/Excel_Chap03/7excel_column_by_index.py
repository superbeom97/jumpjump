### 3.2 단일 워크시트 처리 - 3 특정 열 선택하기 - 열의 인덱스 값을 사용하여 특정 열 선택하기 - 기본 파이썬 코드
## ↳ 관심 있는 열의 인덱스 값을 쉽게 식별할 수 있거나
## ↳ 여러 개의 입력 파일을 처리할 때, 열의 위치가 모든 입력 파일에서 일관성이 있을 때 효과적
## Customer ID와 Purchase Date 열만 필터링

# !/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = [1, 4]

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    for row_index in range(worksheet.nrows):
        row_list = []
        for column_index in my_columns:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)
        data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)