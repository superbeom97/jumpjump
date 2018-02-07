import csv

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))

## 행을 출력하는 함수
def get_csv_rowInstance(row_name, type="int"):
    countRow_index = data[0].index("%s" % row_name)
    countRow_instance = []
    for row in data[1:]:
        countRow_instance.append(int(row[countRow_index]))
    # for i in countRow_instance:   ## 출력까지 하려면
    #     print(i)

    return countRow_instance    ## 이 함수는 가져오는 것만 목적이야! 출력이 아닌!

## 열을 출력하는 함수_type="int" _Ver1
def get_csv_columnInstance(column_name, type="int"):    ## 입력 인수에 초깃값을 미리 설정_p.152
    countColumn_instance = []
    for column in data[1:]:
        if column[0] == column_name:
            countColumn_instance.append(column)

    return countColumn_instance[0][1:]


## 열_Ver2
def get_csv_columnInstance(column_name, type="int"):    ## 입력 인수에 초깃값을 미리 설정_p.152
    countColumn_instance = data[column_name]

    return countColumn_instance


## 행 출력
# print(get_csv_rowInstance("COUNT FEMALE"))  ## 이건 리스트로 출력하는 거

for i in get_csv_rowInstance("COUNT FEMALE"):   ## 이건 하나하나 뽑아 내는 거
    print(i)

## 열_Ver2 출력
# print(get_csv_columnInstance(1))    ## 이건 리스트로 출력하는 거
# print(get_csv_columnInstance(1, 'float'))    ## 초깃값이 설정된 부분을 수정하고 싶을 때_p.153
# print(get_csv_columnInstance(1, 'str'))      ## 초깃값이 설정된 부분을 수정하고 싶을 때

for j in get_csv_columnInstance(1):     ## 이건 하나하나 뽑아 내는 거
    print(j)
for j in get_csv_columnInstance(1, 'float'):    ## 초깃값이 설정된 부분을 수정하고 싶을 때_p.153
    print(j)
for j in get_csv_columnInstance(1, 'str'):      ## 초깃값이 설정된 부분을 수정하고 싶을 때
    print(j)

## 열_Ver1 출력
print(get_csv_columnInstance("10001"))
print(get_csv_columnInstance("10001", 'str'))      ## 초깃값이 설정된 부분을 수정하고 싶을 때
print(get_csv_columnInstance("10001", 'str'))      ## 초깃값이 설정된 부분을 수정하고 싶을 때
