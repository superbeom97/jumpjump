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
    return countRow_instance


## 행 출력
for i in get_csv_rowInstance("COUNT FEMALE"):
    print(i)