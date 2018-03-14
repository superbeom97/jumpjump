### 4.1.2 테이블 내 레코드 갱신하기
## CSV 파일을 사용하여 데이터베이스 테이블에 있는 기존 레코드들을 갱신하는 방법을 알아보자!
## ↳ SQL문만 INSERT 문에서 UPDATE 문으로 변경하면 된다.

# !/usr/bin/env python3
import csv
import sqlite3
import sys

# CSV 입력 파일의 경로와 파일명
input_file = sys.argv[1]

# 메모리에 SQLite3 데이터베이스를 만든다.
# 네 가지 속성을 지닌 sales 테이블을 만든다.
con = sqlite3.connect(':memory:')
query = """CREATE TABLE IF NOT EXISTS sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
con.execute(query)
con.commit()

# sales 테이블에 몇 줄의 데이터를 입력한다.
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()
print("")

# CSV 파일을 읽고, 특정 행의 데이터를 갱신한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)                     ## ↱ 특정 고객(customer)의 amount와 date 값을 갱신
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)     ## UPDATE문은 갱신하고 싶은 레코드와 열 속성을 지정해야 한다.
con.commit()
print("")

# sales 테이블에 질의한다.
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()    ## fetchall() : 모든 결과 데이터를 반환 -> rows라는 리스트 변수에 이 데이터를 할당
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)