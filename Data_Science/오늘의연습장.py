import csv
import math

def get_csv_rowInstance(row_name):                  # 행(row) 입력 함수
    row_instance = []
    row_index = data[0].index(row_name)
    for row_element in data[1:]:
        row_instance.append(row_element[row_index])
    return row_instance

def get_csv_columnInstance(primary_key):            # 열(column) 입력 함수
    column_instance = []
    for column_element in data[1:]:
        if column_element[0] == primary_key:
            column_instance.append(column_element)
    return column_instance

def row_Print(row_instance):                        # 행(row) 출력 함수
    for element_row in row_instance:
        print(element_row)

def column_Print(column_instance):                  # 열(column) 출력 함수
    for element_column in column_instance:
        print(element_column)

def element_row_Print(row_instance):                # 행(row) 요소 출력 함수
    for element_row_print in row_instance:
        print(element_row_print, end=" ")
    print("")

def my_Sum(row_instance):                           # 총합 출력 함수
    element_row_Print(row_instance)
    sum = 0
    for my_sum in row_instance:
        sum += float(my_sum)
    print("총합 : %g" % sum)

def my_Average(row_instance):                       # 평균 출력 함수
    element_row_Print(row_instance)
    sum = 0
    for my_sum in row_instance:
        sum += float(my_sum)
    average_row = sum/len(row_instance)
    print("평균 : %g" % average_row)

def my_Max(row_instance):
    element_row_Print(row_instance)
    max_row = []
    for element_row_max in row_instance:
        max_row.append(float(element_row_max))
    print("최댓값 : %g" % max(max_row))


with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))


my_Max(get_csv_rowInstance("COUNT FEMALE"))