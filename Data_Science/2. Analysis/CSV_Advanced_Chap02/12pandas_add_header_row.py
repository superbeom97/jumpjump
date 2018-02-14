### 2.8 헤더 추가하기 - 팬더스 코드
## 때로는 스프레드시트에 헤어 행이 포함되지 않는 경우가 종종 있다
## 팬더스의 read_csv() 함수를 사용하면 헤더 행이 없는 입력 파일에 열 헤더를 할당하는 작업을 보다 손쉽게 할 수 있다

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
## header=None만 있으면 헤더 행에 0 1 2 3 4 가 쓰임 -> 거기에 이름 names를 지정해서 헤더 행에 쓸 수 있음

data_frame.to_csv(output_file, index=False)