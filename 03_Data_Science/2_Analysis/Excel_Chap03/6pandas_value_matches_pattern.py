### 3.2 단일 워크시트 처리 - 2 특정 행 필터링하기 - 패턴을 활용한 필터링 - 팬더스 코드
## Customer Name 열이 대문자 J로 시작하는 행을 필터링

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()


## startswith() 함수를 사용하여 정규 표현식을 사용하지 않고 데이터를 검색(기본 파이썬 예제에서도 정규 표현식 대신 사용 가능)
### startswith() 함수
## 문자열 데이터 타입에 대해, 대상 문자열이 어떤 문자로 시작하는지를 체크
## print('[Absolutely]'.startswith('A'))
## >> False
## print('[Absolutely]'.startswith('['))
## >> True
## print('[Absolutely]'.startswith('[Abso'))