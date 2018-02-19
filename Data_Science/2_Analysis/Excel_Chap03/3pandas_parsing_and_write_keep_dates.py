### 3.2 단일 워크시트 처리 - 1 엑셀 파일 읽기 및 쓰기 - 날짜 형식 할당 - 팬더스 코드
## 엑셀 통합 문서에는 여러 개의 워크시트가 포함될 수 있지만 그 중 한 워크시트에 포함된 데이터만 필요한 경우

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname='january_2013')    ## 워크시트 'january_2013'을 읽어라

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)    ## 출력하는 엑셀 통합 문서 안에 'jan_2013_output'이라는 워크시트를 추가
writer.save()