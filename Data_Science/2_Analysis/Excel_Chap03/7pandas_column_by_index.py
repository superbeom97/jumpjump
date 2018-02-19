### 3.2 단일 워크시트 처리 - 3 특정 열 선택하기 - 열의 인덱스 값을 사용하여 특정 열 선택하기 - 팬더스 코드
## ↳ 관심 있는 열의 인덱스 값을 쉽게 식별할 수 있거나
## ↳ 여러 개의 입력 파일을 처리할 때, 열의 위치가 모든 입력 파일에서 일관성이 있을 때 효과적

## 팬더스로 특정 열을 선택하는 두 가지 방법이 있다.
## 1. 데이터프레임을 할당하고 [] 안에 선택할 열의 인덱스 값 또는 열의 헤더를 나열하는 방법
## 2. iloc() 함수로 데이터프레임을 지정하는 방법 -> 특정 행과 열을 동시에 선택할 수 있으므로 유용하다.
##   ↳ iloc()를 사용하여 열을 선택하는 경우, 열 인덱스 값 리스트 앞에 ':'를 넣어야 한다.
##     이렇게 하지 않으면 iloc() 함수는 해당 인덱스 값의 행을 필터링할 것이다.

## Customer Name과 Purchase Date 열만 필터링


# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()