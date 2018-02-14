### 3.2 단일 워크시트 처리 - 1 엑셀 파일 읽기 및 쓰기 - xlrd 및 xlwt 모듈을 사용한 기본 파이썬 코드

# !/usr/bin/env python3
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)