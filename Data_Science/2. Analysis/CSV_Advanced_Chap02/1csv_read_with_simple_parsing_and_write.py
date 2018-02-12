### 2.2 CSV 파일 읽고 쓰기(파트1) - 1 csv 모듈을 사용하지 않는 기본 파이썬 코드
## CSV 파일을 읽어서 다른 파일에 그대로 똑같이 쓰기

# !/usr/bin/env python3
import sys  ## sys 모듈은 명령 줄('Run >> Edit Configurations'에서 'Script parameters')에서 추가적으로 입력된 인수를 스크립트로 넘겨준다.
            ## -> supplier_data.csv output_files\\1output

## sys 모듈의 argc 인수 -> 명령 줄 실행 시에 추가적으로 입력되는 인수를 리스트 자료형으로 받는다.
input_file = sys.argv[1]        ## 'supplier_data.csv'를 input_file 변수에 할당
output_file = sys.argv[2]       ## 'output_files\\1output'를 output_file 변수에 할당

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()    ## readline() -> 입력 파일의 첫 번째 행(헤더 행)을 문자열로 읽고, 이를 header 변수에 할당
        header = header.strip()           ## strip() -> header에 있는 문자열의 양끝에서 공백, 탭 및 개행문자 등을 제거, header에 다시 할당
        header_list = header.split(',')   ## split(',') -> 문자열을 쉼표 기준으로 구분하여 리스트에 할당
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')   ## map() -> header_list의 각 원소에 str() 함수를 적용하여 각 원소를 문자열로
        for row in filereader:      ## for문을 사용하여 입력 파일의 나머지 행을 반복
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')