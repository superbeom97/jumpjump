import csv

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))

## 행 입력 함수
def get_csv_rowInstance(row_name, type="int"):
    countRow_index = data[0].index("%s" % row_name)
    countRow_instance = []
    for row in data[1:]:
        countRow_instance.append(int(row[countRow_index]))
    # for i in countRow_instance:   ## 출력까지 하려면
    #     print(i)

    return countRow_instance    ## 이 함수는 가져오는 것만 목적이야! 출력이 아닌!

## 열 입력 함수
def get_csv_columnInstance(column_name, type="int"):    ## 입력 인수에 초깃값을 미리 설정_p.152
    countColumn_instance = data[column_name]

    return countColumn_instance

## 행 출력 함수
def print_row(row_instant, type="int"):
    countRow_instant = []
    for i in get_csv_rowInstance(row_instant):
        countRow_instant.append(i)

    return print(countRow_instant)

## 열 출력 함수
def print_column(column_instant, type="int"):
    countColumn_instant = []
    for i in get_csv_columnInstance(column_instant):
        countColumn_instant.append(i)

    return print(countColumn_instant)


## 행 출력
print_row("COUNT FEMALE")
print_row("COUNT FEMALE", type="float")
print_row("COUNT FEMALE", type="str")

## 열_Ver2 출력
print_column(1)