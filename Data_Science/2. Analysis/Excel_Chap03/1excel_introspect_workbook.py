## xlrd / xlwt 모듈 설치
## cmd 창에서 -> py -m pip install xlrd
##            -> py -m pip install xlwt

### 3.1 엑셀 통합 문서 내부 살펴보기 - 기본 파이썬 코드

# !/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)