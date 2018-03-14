### 3.2 단일 워크시트 처리 - 1 엑셀 파일 읽기 및 쓰기 - 날짜 형식 할당 - 기본 파이썬 코드
## 엑셀 통합 문서에는 여러 개의 워크시트가 포함될 수 있지만 그 중 한 워크시트에 포함된 데이터만 필요한 경우
## ↳ 2excel_parsing_and_write.py_날짜가 날짜 대신 숫자(날짜 형식이 아닌)로 표시됨 -> 날짜 형식으로 포매팅

# !/usr/bin/env python3
import sys
from datetime import date   ## 값을 날짜로 변환하고 날짜 형식으로 포매팅할 수 있게 한다
from xlrd import open_workbook, xldate_as_tuple
## xldate_as_tuple() : 날짜, 시간, 날짜+시간을 나타내는 엑셀의 숫자를 튜플로 변환할 수 있다
## 숫자를 튜플로 변환하면 특정 날짜 요소(예, 년, 월, 일)를 추출하여 다른 날짜 형식(예, 1/1/2018 또는 January 1,2018)으로 포매팅할 수 있다.
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, col_index) == 3:  ## 셀 유형이 3번인지 판별_셀 유형 3은 날짜 셀 -> 각 셀에 날짜가 들어 있는지 판별
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                ## print(date_cell) >> (2013, 1, 18, 0, 0, 0)
                ## worksheet.cell_value(row_index, col_index) : 부동소수점 숫자를 날짜로 나타내는 튜플로 변환
                ## workbook.datemode : 날짜를 확인하여 올바르게 튜플로 변환하기 위해서
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')  ## strftime() : 날짜 객체를 할당된 날짜 형식의 문자열로 변환
                ## print(date_cell) >> 01/18/2013
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                output_worksheet.write(row_index, col_index, non_date_cell)
output_workbook.save(output_file)