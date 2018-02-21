### 4.1 파이썬 내장 모듈 sqlite3
## 파이썬 내장 모듈인 sqlite3 모듈 이용 -> 파이썬 코드로 인메모리 데이터베이스와 데이터가 채워진 테이블을 생성하여 실습
## 데이터베이스 테이블을 만들고, 여기에 데이터를 삽입하고, 출력될 데이터의 수를 합치고 계산
## SQL 쿼리가 출력한 행의 수(데이터의 수)를 세보자

# !/usr/bin/env python3
import sqlite3  ## 별도의 서버 처리 과정이 필요 없는 디스크 기반의 가벼운 데이터베이스를 제공,
                ## 여러 종류의 SQL 쿼리 언어를 사용하여 데이터베이스에 접근할 수 있게 해준다.

# 메모리에 SQLite3 데이터베이스를 만든다.
# 네 가지 속성을 지닌 sales 테이블을 만든다.
                                    ## :memory:는 휘발성, 여기서만 사용하고 삭제되는 -> 저장하려면 다른 문자열 사용해야 한다.
con = sqlite3.connect(':memory:')   ## sqlite3을 이용하려면 데이터베이스를 나타내는 접속 객체(con)를 생성해야 한다.
query = """CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
con.execute(query)  ## 접속 객체의 execute() 함수 : query 변수에 들어 있는 SQL 명령어를 실행 -> 인메모리 데이터베이스 내에 sales 테이블이 만들어진다.
con.commit()    ## commit() 함수 : 데이터베이스의 변화를 저장 -> 사용하지 않으면 변경된 상태가 데이터베이스에 반영되지 않는다.

# sales 테이블에 데이터를 삽입한다.
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]     ## ↱ 물음표(?) : SQL 명령어에서 사용하려는 변수들의 위치를 표시하는 플레이스홀더 역할
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"  ## SQL 명령어 - data 변수에 포함된 여러 행의 데이터를 sales 테이블에 삽입하기 위한 INSERT 구문
                                                    ## ↳ execute() 또는 executemany() 함수에 변수들로 구성된 튜플을 전달하고, 이때 튜플 내의 각 변수가 SQL 명령어 내 위치에 대입된다.
con.executemany(statement, data)    ## executemany() 함수를 이용하여 data에 포함된 모든 튜플 데이터에 대해, statement에 있는 SQL 명령어를 실행
con.commit()                        ## ↳ data에는 네 개의 튜플이 있으므로, executemany()는 네 번의 INSERT 명령을 실행하여 sales 테이블에 네 행의 데이터를 삽입한다.

## < 데이터베이스 테이블로부터 데이터를 얻는 방법에 대해 알아보자! >
# sales 테이블에 질의한다.
cursor = con.execute("SELECT * FROM sales")     ## 한 줄의 명령어를 실행하려면 execute 함수를 이용하고, 그 결과를 cursor에 할당
rows = cursor.fetchall()    ## fetchall() : 모든 결과 데이터를 반환 -> rows라는 리스트 변수에 이 데이터를 할당

# 출력된 데이터의 수를 센다.
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))


## 해설
# query = """CREATE TABLE sales             SQL 명령어 - 데이터베이스에 sales라는 테이블 생성
#             (customer VARCHAR(20),        sales 테이블은 customer, product, amount, date라는 이름의 4가지 속성을 지닌다.
#             product VARCHAR(40),          customer 속성은 최대 길이가 20자인 문자열 필드
#             amount FLOAT,                 amount 속성은 실수 형식 필드
#             date DATE);"""                date 속성은 날짜 형식 필드

# data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),             ## 튜플로 이루어진 리스트를 만들어 data라는 변수에 할당
#         ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),                  ## 리스트 내 각 원소는 4개의 변수를 포함한 하나의 튜플
#         ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
#         ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]