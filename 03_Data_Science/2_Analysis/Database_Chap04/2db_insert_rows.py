#### CSV 입력 파일들을 사용하여, 대규모로 레코드를 테이블에 삽입하고 갱신하는 방법 등을 알아보자!

### 4.1.1 테이블에 새 레코드 삽입하기
## CSV 파일을 사용하여 대규모 데이터를 데이터베이스 테이블에 입력하는 방법을 알아보자!
## ↳ 데이터베이스 테이블을 만들고, CSV 파일의 데이터를 테이블에 입력하고, 새롭게 입력된 데이터를 출력해보자!

# !/usr/bin/env python3
import csv          ## CSV 입력 파일을 읽고 파싱하는 함수들을 사용할 수 있게 한다.
import sqlite3
import sys          ## 파일 경로와 파일명을 명령 줄에서 받아올 수 있게 한다.

# CSV 입력 파일의 경로와 파일명
input_file = sys.argv[1]

# 메모리에 SQLite3 데이터베이스를 만든다.
# 다섯 가지 속성을 지닌 Supplier 테이블을 만든다.
con = sqlite3.connect('Suppliers.db')   ## 'Suppliers.db'라는 로컬 데이터베이스에 연결
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);"""     ## 다섯 가지 속성을 지닌 Suppliers라는 테이블을 만든다
c.execute(create_table)
con.commit()

# CSV 파일을 읽는다.
# 읽은 데이터를 Suppliers 테이블에 삽입한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:     ## 모든 행을 반복 처리
    data = []   ## 입력 데이터의 각 행별로, 이 data 변수에 INSERT 구문에 필요한 값들을 채울 것이다.
    for column_index in range(len(header)):     ## 모든 속성을 반복 처리할 for문
        data.append(row[column_index])
    print(data)                           ## ↱ 물음표 위치에 대입되는 값들은 쉼표 뒤에 있는 data 변수에 할당된 값 리스트에 들어 있다.
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)    ## Suppliers 테이블에 한 행의 변수들을 입력하는 INSERT 구문 실행
con.commit()                              ## ↳ 물음표의 수는 입력 파일에 있는 열의 수와 일치해야 하고, 테이블의 열의 수와도 일치해야 한다.
print("")                                 ## ↳ 입력 파일 내 열의 순서는 테이블 내 열의 순서와 일치해야 한다.

# Suppliers 테이블에 질의한다.
output = c.execute("SELECT * FROM Suppliers")   ## Suppliers 테이블의 모든 데이터를 선택하는 SQL문 실행
rows = output.fetchall()    ## 그 결과(output)의 행들을 변수 rows에 가져온다.
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)