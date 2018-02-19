import csv

## 행의 입력 정의
def get_csv_rowInstance(row_name):
    row_instance = []
    row_index = data[0].index(row_name)

    for row in data[1:]:
        row_instance.append(row[row_index])

    return row_instance

## 열의 입력 정의
def get_csv_columnInstance(primary_key):
    column_instance = []
    for column in data[1:]:
        if column[0] == primary_key:
            column_instance.append(column)

    return column_instance[0]

## 행의 출력 정의
def print_row(row_instance, type="int"):
    if type == "int":
        list(map(int, row_instance))
    elif type == "float":
        list(map(float, row_instance))

    for row_element in row_instance:
        print(row_element)

## 열의 출력 정의
def print_column(column_instance):
    for column_element in column_instance:
        print(column_element)


with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))


while True:
    access = int(input("데이터 유형을 선택하시오 \n(열: 1, 행: 2, 종료: 3) : "))

    if access == 1:
        access_key = int(input("열의 Access Key를 입력하시오: "))
        print_column(get_csv_columnInstance("%s" % access_key))
        continue

    elif access == 2:
        access_key = input("행의 Access Key를 입력하시오: ")
        print_row(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 3:
        print("이용해 주셔서 감사합니다!")
        break