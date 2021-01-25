# DB 자료( RDBMS ) 연동 후  DataFrame 으로 객체화
# sqllite3
import sqlite3

sql = "create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"

conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('kbs.db')
conn.execute(sql)
conn.commit()

data = [('mouse', 'samsung', 12.5, 15000), ('keyboard', 'lg', 500.5, 55000)]
stmt = "insert into test values(?,?,?,?)"
conn.executemany(stmt, data)
data1 = ('book', 'hanbit', 1000, 35000)
conn.execute(stmt, data1)
data2 = 'pen', 'monami', 100, 1000
conn.execute(stmt, data2)
conn.commit()

cursor = conn.execute("select * from test")
rows = cursor.fetchall()

for a in rows:
    print(a)
    
print('\ntest 테이블 자료를 DataFrame 으로 저장\n')
import pandas as pd
#df1 = pd.DataFrame(rows, columns=['상품명', '제조사', '무게', '가격'])
df1 = pd.DataFrame(rows, columns=list(zip(*cursor.description))[0])
print(df1)
#print(*cursor.description)

print()
df2 = pd.read_sql("select * from test", conn)
print(df2)

cursor.close()
conn.close()

    
print('-----------------------')

# DataFrame 을 DB로 저장하기
data = {
    'irum':['신기해','홍길동','강나루'],
    'nai':[22,25,34],
}

frame = pd.DataFrame(data)
conn = sqlite3.connect("test.db")
frame.to_sql("mytable", conn, if_exists="append", index=False)

#읽기
df3 = pd.read_sql("select * from mytable", conn)
print(df3)


    