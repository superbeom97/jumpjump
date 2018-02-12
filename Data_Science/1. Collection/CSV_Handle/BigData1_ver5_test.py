import csv
import math

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

## row_instance 출력 함수
def Row_instance_print(row_instance):
    for i in row_instance:
        print(i, end=" ")
    print("")

## 총합 함수 정의
def my_Sum(row_instance):
    Row_instance_print(row_instance)

    sum = 0
    for i in row_instance:
        if type(i) == int:
            sum += int(i)
        else:
            sum += float(i)
    print("총합 : %s" % sum)

## 평균 함수 정의
def my_Average(row_instance):
    print("평균(Average) 공식 : 표본의 합 / 표본의 수")
    Row_instance_print(row_instance)

    sum = 0
    for i in row_instance:
        if type(i) == int:
            sum += int(i)
        else:
            sum += float(i)

    average = sum/len(row_instance)
    print("평균 : %s" % average)

## 최댓값 함수 정의
def my_Max(row_instance):
    Row_instance_print(row_instance)

    max_row = []
    for i in row_instance:
        if type(i) == int:
            max_row.append(int(i))
        else:
            max_row.append(float(i))
    print("최댓값 : %s" % max(max_row))

## 최솟값 함수 정의
def my_Min(row_instance):
    Row_instance_print(row_instance)

    min_row = []
    for i in row_instance:
        if type(i) == int:
            min_row.append(int(i))
        else:
            min_row.append(float(i))
    print("최솟값 : %s" % min(min_row))

## 편차 함수 정의
def my_Deviation(row_instance):
    print("편차(Deviation)의 공식 : 표본 - 평균")

    sum = 0
    for i in row_instance:
        if type(i) == int:
            sum += int(i)
        else:
            sum += float(i)
    average = sum/len(row_instance)

    print("표본 편차")
    for j in row_instance:
        if type(j) == int:
            minus_average = int(j) - average
        else:
            minus_average = float(j) - float(average)

        print("%s %s" % (j, minus_average))

## 표준편차 함수 정의
def my_Standard_Deviation(row_instance):
    print("표준편차(Standard Deviation) 공식 : √분산")

    Row_instance_print(row_instance)

    square_average_list = []
    for i in row_instance:
        square_i = 0
        if type(i) == int:
            square_i = int(i) * int(i)
        else:
            square_i = float(i) * float(i)

        square_average_list.append(square_i)

    square_sum = 0
    for z in square_average_list:
        if type(z) == int:
            square_sum += int(z)
        else:
            square_sum += float(z)
    square_average = square_sum / len(square_average_list)

    sum = 0
    for j in row_instance:
        if type(j) == int:
            sum += int(j)
        else:
            sum += float(j)
    average = sum / len(row_instance)
    average_square = average * average

    variance_row = square_average - average_square
    standard_deviation = math.sqrt(variance_row)

    print("표준편차 : %s" % standard_deviation)


## 분산 함수 정의
def my_Variance(row_instance):
    print("분산(Variance) 공식 : (제곱의 평균) - (평균의 제곱)")
    Row_instance_print(row_instance)

    square_average_list = []
    for i in row_instance:
        square_i = 0
        if type(i) == int:
            square_i = int(i) * int(i)
        else:
            square_i = float(i) * float(i)
        square_average_list.append(square_i)

    square_sum = 0
    for z in square_average_list:
        if type(z) == int:
            square_sum += int(z)
        else:
            square_sum += float(z)
    square_average = square_sum/len(square_average_list)

    sum = 0
    for j in row_instance:
        if type(j) == int:
            sum += int(j)
        else:
            sum += float(j)
    average = sum / len(row_instance)
    average_square = average * average

    variance_row = square_average - average_square

    print("분산 : %s" % variance_row)

## 오름차순 정렬 함수 정의
def my_Ascendant(row_instance):
    Row_instance_print(row_instance)

    ascendant_row = []
    for i in row_instance:
        if type(i) == int:
            ascendant_row.append(int(i))
        else:
            ascendant_row.append(float(i))

    ascendant_row.sort()
    print("<<오름차순 정렬>>")
    for z in ascendant_row:
        print(z, end=" ")
    print("")

## 내림차순 정렬 함수 정의
def my_Descendant(row_instance):
    Row_instance_print(row_instance)

    descendant_row = []
    for i in row_instance:
        if type(i) == int:
            descendant_row.append(int(i))
        else:
            descendant_row.append(float(i))

    descendant_row.sort()
    descendant_row.reverse()
    print("<<내림차순 정렬>>")
    for z in descendant_row:
        print(z, end=" ")
    print("")


with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))


while True:
    access = int(input("데이터 유형을 선택하시오 \n(열: 1, 행: 2, 총합: 3, 평균: 4, 최댓값: 5, 최소값: 6, 편차: 7, 표준편차: 8, 분산: 9, 오름차순 정렬: 10, 내림차순 정렬: 11, 종료: 12) : "))

    if access == 1:
        access_key = int(input("열의 Access Key를 입력하시오: "))
        print_column(get_csv_columnInstance("%s" % access_key))
        continue

    elif access == 2:
        access_key = input("행의 Access Key를 입력하시오: ")    ## ex) COUNT FEMALE
        print_row(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 3:
        access_key = input("총합을 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Sum(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 4:
        access_key = input("평균을 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Average(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 5:
        access_key = input("최댓값을 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Max(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 6:
        access_key = input("최솟값을 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Min(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 7:
        access_key = input("편차를 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Deviation(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 8:
        access_key = input("표준편차를 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Standard_Deviation(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 9:
        access_key = input("표준편차를 구하고자 하는 행의 Access Key를 입력하시오: ")
        my_Variance(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 10:
        access_key = input("오름차순 정렬하고자 하는 행의 Access Key를 입력하시오: ")
        my_Ascendant(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 11:
        access_key = input("내림차순 정렬하고자 하는 행의 Access Key를 입력하시오: ")
        my_Descendant(get_csv_rowInstance("%s" % access_key))
        continue

    elif access == 12:
        print("이용해 주셔서 감사합니다!")
        break