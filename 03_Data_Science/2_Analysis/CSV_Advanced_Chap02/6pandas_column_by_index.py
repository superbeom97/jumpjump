### 2.6 특정 열 선택하기 - 2.6.1 열의 인덱스 값을 사용하여 특정 열을 선택하는 방법 - 팬더스 코드
## 이 방법은 열의 인덱스 값을 쉽게 식별할 수 있거나 여러 개의 입력 파일을 처리할 때,
## 또는 모든 입력 파일에서 열의 위치가 변경 되지 않는 경우에 효과적
## -> Supplier Name 및 Cost 열만 포함해 보자

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)                        ## iloc는 정수 기반 위치(integer location)라는 뜻
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]     ## iloc 명령을 사용하여 인덱스 값을 기반으로 열을 선택
data_frame_column_by_index.to_csv(output_file, index=False)