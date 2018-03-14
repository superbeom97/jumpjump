### 3.5 여러 개의 통합 문서 처리하기 - 1 통합 문서의 개수 및 각 통합 문서의 행과 열 개수 세기 - 기본 파이썬 코드

# !/usr/bin/env python3
import glob
import os
import sys
from xlrd import open_workbook

input_directory = sys.argv[1]

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook: {}'.format(os.path.basename(input_file)))
    print('Numner of worksheets: {}'.format(workbook.nsheets))
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)
    workbook_counter += 1
print('Number of Excel workbooks: {}'.format(workbook_counter))