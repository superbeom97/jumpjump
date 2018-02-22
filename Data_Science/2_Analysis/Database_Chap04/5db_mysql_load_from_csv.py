## py -m pip install mysqlclient 설치 -> import MySQLdb를 사용할 수 있음
## ↳ 파이썬이 데이터베이스 또는 데이터베이스의 개별 테이블고 ㅏ상호작용할 수 있도록 해준다!!

### 4.2 MySQL 데이터베이스 - 1 테이블에 새 레코드 입력하기
## CSV 파일의 데이터를 앞서 만든 데이터베이스 테이블에 입력하고, 테이블에 있는 데이터를 출력해 보자!

# !/usr/bin/env python3
import csv
import MySQLdb  ## MySQL 데이터베이스와 테이블에 연결하는 함수를 사용할 수 있게 한다.
import sys
from datetime import datetime, date

# CSV 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다.      ## ↱ 데이터베이스에 접속하기 위해서는 host, port, db, user, passwd 등 일반적인 인수들을 설정해야 한다.
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')    ## host : 데이터베이스가 위치한 컴퓨터의 호스트 주소
c = con.cursor()        ## port : MySQL 서버의 TCP/IP 접속을 위한 포트 번호 - 기본적으로 3306    ## db : 접속할 데이터베이스의 이름
                        ## user : 데이터베이스에 접속할 사용자 이름        ## passwd : 루트 계정에 대한 비밀번호
## ↳ con.cursor() : my_suppliers 데이터베이스의 Suppliers 테이블에서 SQL문을 실행하고
##                 그 변화를 데이터 베이스에 저장하는 데 이용할 수 있게 한다.

# 파일 읽기
# Suppliers 테이블에 데이터를 입력한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:    ## ↱ 해당 열의 값을 문자열로 변환하고, 달러($) 기호가 있으면 제거하고, 리스트 변수인 data에 저장
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            # %Y를 쓰면 연도를 2016으로 저장하고, %y를 쓰면 16로 저장한다.
            ## 근데 %Y 쓰면 오류 -> %y 써줘야 함!!
            a_date = a_date.strftime('%y-%m-%d')    ## 새로운 입력 형식의 문자열로 변환
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)   ## 데이터베이스 테이블에 각 행별 데이터를 입력
con.commit()
print("")

# Suppliers 테이블에 질의한다.
c.execute("SELECT * FROM Suppliers")    ## Suppliers 테이블의 모든 데이터를 선택하는 SQL 문을 실행하고,
rows = c.fetchall()             ## 그 결과 행들을 변수 rows에 가져온다.
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)