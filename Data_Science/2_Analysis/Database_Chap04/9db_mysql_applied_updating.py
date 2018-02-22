### MySQL 데이터베이스 - 테이블 내 레코드 갱신하고 CSV 파일로 출력하기

# !/usr/bin/env python3
import csv
import MySQLdb
import sys

# CSV 입력 파일 경로와 파일명
input_file = sys.argv[1]
output_file = sys.argv[2]

# MySQL 데이터베이스에 접속한다,          ## ↱ MySQLdb의 connect() 함수를 이용, MySQL 데이터베이스인 my_suppliers에 접속
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()     ## 데이터베이스 테이블에서 SQL 문을 실행하고 그 결과를 저장하기 위한 커서를 만든다.

# CSV 파일을 읽고 특정 행을 갱신한다.
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)         ## ↱ Supplier Name에 대해 Cost와 Purchase Date 속성을 갱신하려고 함
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
con.commit()

# 파일 객체를 만들고, 헤더 행을 작성한다.
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

# Suppliers 테이블을 검색하고 결과를 CSV 파일에 쓴다.
c.execute("""SELECT * FROM Suppliers;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)