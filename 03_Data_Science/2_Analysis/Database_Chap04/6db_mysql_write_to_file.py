### 4.2 MySQL 데이터베이스 - 2 테이블 검색 및 결과물을 CSV 파일로 출력하기
## Suppliers 데이터베이스 테이블에서 특정 레코드를 검색하고, 이 결과를 CSV 파일로 저장해 보자!
## ↳ Cost열이 700보다 큰 레코드를 출력해 보자!

# !/usr/bin/env python3
import csv
import MySQLdb
import sys

# CSV 입력 파일 경로와 파일명
output_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다.,            ## ↱ MySQLdb의 connect() 함수를 이용, MySQL 데이터베이스인 my_suppliers에 접속
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()    ## 데이터베이스 테이블에서 SQL 문을 실행하고 그 결과를 저장하기 위한 커서를 만든다.

# 파일 객체를 만들고, 헤더 행을 작성한다.
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

# Suppliers 테이블을 검색하고 결과를 CSV 파일에 쓴다.
c.execute("""SELECT *
          FROM Suppliers
          WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)