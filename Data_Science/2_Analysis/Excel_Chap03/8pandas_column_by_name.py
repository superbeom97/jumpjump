### 3.2 단일 워크시트 처리 - 3 특정 열 선택하기 - 열 헤더를 사용하여 특정 열 선택하기 - 팬더스 코드
## ↳ 선택하려는 열의 이름을 쉽게 식별할 수 있거나
## ↳ 여러 입력 파일을 처리할 때 열 헤더 내용 자체는 입력 파일 전체에서 일관되지만, 열의 위치는 일치하지 않는 경우 효과적

## 팬더스에서 열 헤더를 기반으로 특정 열을 선택하려면 데이터프레임 뒤에 [] 안에 열 헤더를 문자열로 넣으면 된다.
## 또는 loc() 함수를 사용할 수 있다. -> loc() 함수를 사용하여 열을 선택하는 경우에는 열 헤더 리스트 앞에 ':'을 추가해야 한다.
## Customer Name과 Purchase Date 열만 필터링

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]
## data_frame_column_by_name = data_frame['Customer ID']  -> 열 헤더 하나는 되는데 2개 이상은 모르겠음

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()