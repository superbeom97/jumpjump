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
## startswith() 함수를 사용하여 정규 표현식을 사용하지 않고 데이터를 검색(기본 파이썬 예제에서도 정규 표현식 대신 사용 가능)
data_frame_value_matches_pattern.to_csv(output_file, index=False)


### startswith() 함수
## 문자열 데이터 타입에 대해, 대상 문자열이 어떤 문자로 시작하는지를 체크
## print('[Absolutely]'.startswith('A'))
## >> False
## print('[Absolutely]'.startswith('['))
## >> True
## print('[Absolutely]'.startswith('[Abso'))
