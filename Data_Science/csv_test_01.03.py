import csv
import math

def get_csv_rowInstance(row_name):  # 행(row) 입력 함수
    row_instance = []
    row_index = data[0].index(row_name)
    for element_row in data[1:]:
        row_instance.append(element_row[row_index])
    return row_instance

def get_csv_columnInstance(primary_key):    # 열(column) 입력 함수
    column_instance = []
    for element_column in data[1:]:
        if element_column[0] == primary_key:
            column_instance.append(element_column)
    return column_instance[0]

def row_Print(row_instance):    # 행(row) 출력 함수
    for element_row_print in row_instance:
        print(element_row_print)

def column_Print(element_instance):     # 열(column) 입력 함수
    for element_column_print in element_instance:
        print(element_column_print)

def element_row_Print(row_instance):    # 행(row) 요소 출력 함수
    print("<<선택하신 access key값의 요소는 다음과 같습니다>>")
    for element_row_print in row_instance:
        print(element_row_print, end=" ")
    print("")

def my_Sum(row_instance):               # 총합 함수
    element_row_Print(row_instance)
    sum = 0
    for element_row in row_instance:
        sum += float(element_row)
    print("총합 : %g" %sum)

def my_Average(row_instance):           # 평균 함수
    element_row_Print(row_instance)
    sum = 0
    for element_row in row_instance:
        sum += float(element_row)
    average_row = sum/len(row_instance)
    print("평균 : %g" % average_row)

def my_Max(row_instance):               # 최댓값 함수
    element_row_Print(row_instance)
    max_row = []
    for element_row in row_instance:
        max_row.append(float(element_row))
    print("최댓값 : %g" % max(max_row))

def my_Min(row_instance):               # 최솟값 함수
    element_row_Print(row_instance)
    min_row = []
    for element_row in row_instance:
        min_row.append(float(element_row))
    print("최댓값 : %g" % min(min_row))

def my_Deviation(row_instance):         # 편차 함수
    element_row_Print(row_instance)
    sum = 0
    for element_row in row_instance:
        sum += float(element_row)
    average_row = sum / len(row_instance)

    print("표본       편차")
    for element_row_j in row_instance:
        print("%-3g      %3g" % (float(element_row_j), (float(element_row_j)-average_row)))
        ## %3g는 전체 길이가 3개인 문자열 공간에서 오른쪽 정렬하고, 그 앞의 나머지는 공백으로
        ## %-3g는 전체 길이가 3개인 문자열 공간에서 왼쪽 정렬하고, 그 뒤의 나머지는 공백으로

def my_Variance(row_instance):      # 분산 입력 함수
    #제곱의 평균 - 평균의 제곱
    element_row_Print(row_instance)
    square_one = 0
    average_one = 0
    for element_row in row_instance:
        square_one += float(element_row)*float(element_row)
        average_one += float(element_row)

    square_one_average = square_one/len(row_instance)
    average_two = average_one/len(row_instance)
    average_two_square = average_two*average_two
    variance_row = square_one_average - average_two_square
    return variance_row

def my_Variance_Print(variance_row):    # 분산 출력 함수
    print("편차 : %g" % (variance_row))

def my_Standard_Deviation(variance_row):    # 표준편차 출력 함수
    print("표준편차 : %g" % math.sqrt(variance_row))

def my_Cendant(row_instance):       # 오름차순/내림차순 입력 함수
    element_row_Print(row_instance)
    cendant_row = []
    for element_row in row_instance:
        cendant_row.append(float(element_row))
    cendant_row.sort()
    return cendant_row

def my_Ascendant(cendant_row):      # 오름차순 출력 함수
    print("<<오름차순 정렬>>")
    for z in cendant_row:
        print("%g" % z, end=" ")
    print("")

def my_Descendant(cendant_row):     # 내림차순 출력 함수
    cendant_row.reverse()
    print("<<내림차순 정렬>>")
    for z in cendant_row:
        print("%g" % z, end=" ")
    print("")


with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))


while True:
    number = int(input("<<원하는 서비스를 선택하시오>> \n열:1, 행:2, 총합:3, 평균:4, 최댓값:5, 최솟값:6, 편차:7, 분산:8, 표준편차:9, 오름차순:10, 내림차순:11, 종료:12\n=> "))

    if number == 1:
        access_key = input("구하고자 하는 열의 access key값을 입력하시오: ")
        column_Print(get_csv_columnInstance("%s" %access_key))

    elif number == 2:
        access_key = input("구하고자 하는 행의 access key값을 입력하시오: ")
        row_Print(get_csv_rowInstance("%s" % access_key))

    elif number == 3:
        access_key = input("총합을 원하는 행의 access key값을 입력하시오: ")
        my_Sum(get_csv_rowInstance("%s" % access_key))

    elif number == 4:
        access_key = input("평균을 원하는 행의 access key값을 입력하시오: ")
        my_Average(get_csv_rowInstance("%s" % access_key))

    elif number == 5:
        access_key = input("최댓값을 원하는 행의 access key값을 입력하시오: ")
        my_Max(get_csv_rowInstance("%s" % access_key))

    elif number == 6:
        access_key = input("최솟값을 원하는 행의 access key값을 입력하시오: ")
        my_Min(get_csv_rowInstance("%s" % access_key))

    elif number == 7:
        access_key = input("편차를 원하는 행의 access key값을 입력하시오: ")
        my_Deviation(get_csv_rowInstance("%s" % access_key))

    elif number == 8:
        access_key = input("분산을 원하는 행의 access key값을 입력하시오: ")
        my_Variance_Print(my_Variance(get_csv_rowInstance("%s" % access_key)))

    elif number == 9:
        access_key = input("표준편차를 원하는 행의 access key값을 입력하시오: ")
        my_Standard_Deviation(my_Variance(get_csv_rowInstance("%s" % access_key)))

    elif number == 10:
        access_key = input("오름차순을 원하는 행의 access key값을 입력하시오: ")
        my_Ascendant(my_Cendant(get_csv_rowInstance("%s" % access_key)))

    elif number == 11:
        access_key = input("내림차순을 원하는 행의 access key값을 입력하시오: ")
        my_Descendant(my_Cendant(get_csv_rowInstance("%s" % access_key)))

    elif number == 12:
        print("이용해 주셔서 감사합니다!!")
        break