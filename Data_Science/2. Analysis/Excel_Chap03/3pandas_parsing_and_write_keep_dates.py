### 3.2 단일 워크시트 처리 - 1 엑셀 파일 읽기 및 쓰기 - 날짜 형식 할당 - 팬더스 코드

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()