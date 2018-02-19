### 3.2 단일 워크시트 처리 - 1 엑셀 파일 읽기 및 쓰기 - xlrd 및 xlwt 모듈을 사용한 기본 파이썬 코드
## 엑셀 통합 문서에는 여러 개의 워크시트가 포함될 수 있지만 그 중 한 워크시트에 포함된 데이터만 필요한 경우
## ↳ 날짜가 날짜 대신 숫자(날짜 형식이 아닌)로 표시됨 -> 날짜 형식으로 포매팅_3excel_parsing_and_write_keep_dates.py

# !/usr/bin/env python3
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()    ## xlwt의 Workbook 객체를 인스턴스화하여 결과를 출력하여 엑셀 통합 문서에 쓸 수 있다.
output_worksheet = output_workbook.add_sheet('jan_2013_output')
## xlwt의 add_sheet() : 출력하는 엑셀 통합 문서 안에 'jan_2013_output'이라는 워크시트를 추가

with open_workbook(input_file) as workbook:     ## open_workbook() : 입력되는 엑셀 통합 문서를 workbook 객체로 연다
    worksheet = workbook.sheet_by_name('january_2013')  ## sheet_by_name() : 'january_2013'이라는 이름의 워크시트에 연결
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))  ## worksheet.cell_value(row_index, column_index)) 값 가져오는 거~
output_workbook.save(output_file)