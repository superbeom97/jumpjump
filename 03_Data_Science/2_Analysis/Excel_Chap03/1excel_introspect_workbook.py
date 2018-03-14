## xlrd / xlwt 모듈 설치
## cmd 창에서 -> py -m pip install xlrd
##            -> py -m pip install xlwt

### 3.1 엑셀 통합 문서 내부 살펴보기 - 기본 파이썬 코드
## 통합 문서의 워크시트 개수, 워크시트 이름 및 각 워크시트의 행과 열 수를 확인

# !/usr/bin/env python3
import sys
from xlrd import open_workbook      ## 엑셀 파일을 읽고 파싱하는 데 사용할 수 있게 함

input_file = sys.argv[1]

workbook = open_workbook(input_file)    ## open_workbook() 함수 사용 -> 엑셀 입력 파일을 workbook 변수의 객체로 연다
## ↳ workbook 객체에는 엑셀 통합 문서에 대한 사용 가능한 모든 정보가 포함되어 있으므로 개별 워크시트를 검색하는 데 사용할 수 있다
print('Number of worksheets:', workbook.nsheets)    ## .nsheets 사용
for worksheet in workbook.sheets():  ## .sheets()는 엑셀 통합 문서 내의 개별 워크시트를 식별하는 데 사용
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
    ## .name : 각 워크시트의 이름을 식별
    ## .nrows : 각 워크시트의 행 수를 식별
    ## .ncols : 각 워크시트의 열 수를 식별