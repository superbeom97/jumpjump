### 2.7 연속된 행 선택하기 - 팬더스 코드
## 때론 분석해야 하는 파일 맨 위 또는 맨 아래에 처리할 필요가 없는 애용이 포함되어 있다.
## 예를 들어 파일의 맨 위에 문서 제목과 작성자를 쓴 행이 있거나 파일의 맨 아래에 출처, 주의사항, 메모 등이 있는 경우
## -> 파일의 맨 위, 열 헤더가 있는 행 위에 세 개 행을 삽입 - I don't care about this line 식으로 필요 없는 텍스트 추가
## 맨 아래, 즉 마지막 데이터 행 아래 세 행에도 마찬가지로 필요 없는 덱스트 추가 - I don't want this line either

# !/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)