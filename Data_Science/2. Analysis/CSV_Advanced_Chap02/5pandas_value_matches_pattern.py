### 2.5.3 패턴/정규 표현식을 활용한 필터링 - 팬더스 코드
## 특정한 패턴과 일치하거나 패턴이 포함되어 있는 (즉, 정규 표현식) 행을 선택하여 하위 데이터셋으로 만들어야 하는 경우가 있다
## 이런 경우 행의 데이터 값이 패턴과 일치하는지 혹은 패턴을 포함하는지를 판별한 뒤, 그 행을 필터링한다
## -> Invoice Number 열의 데이터 값이 '001-'로 시작하는 행을 선택하고 결과를 출력 파일에 쓴다

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)