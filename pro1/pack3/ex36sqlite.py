#sqlite3: 내장된 개인용 databse

import sqlite3

print(sqlite3.sqlite_version_info)
print()

conn = sqlite3.connect('kbs.db')        #db가 파일로 생성
conn = sqlite3.connect(':memory:')  #db가 ram에 저장

try:
    cur = conn.cursor()             # sql 문 처리가 가능
    
    
    
    #테이블 작성
    cur.execute("create table if not exists friends(name text, phone text, addr text)")
    
    #자료 입력
    cur.execute("insert into friends(name, phone, addr) values ('한국인', '111-1111', '서울')")
    cur.execute("insert into friends(name, phone, addr) values ('지구인', '111-2222', '서울')")
    cur.execute("insert into friends(name, phone, addr) values ('고길동', '222-2222', '경기')")
    cur.execute("insert into friends(name, phone, addr) values (?,?,?)",('신기해', '222-1111', '김포'))
    inputdata = ('손오공', '111-4444', '마포')
    cur.execute("insert into friends(name, phone, addr) values(?,?,?)", inputdata)
    conn.commit()
    
    #자료 읽기
    cur.execute("select * from friends")
    #print(cur.fetchone())
    #print(cur.fetchall())            # 리스트 안에 튜플로 존재. [('한국인', '111-1111', '서울'), ('지구인', '111-2222', '서울'), ('고길동', '222-2222', '경기'), ('신기해', '222-1111', '김포'), ('손오공', '111-4444', '마포')]
    
    for r in cur:
        print(r[0] + ' ' + r[1]+ ' ' + r[2])
        
    
    
except Exception as e:
    print('err : ' + str(e))
    conn.rollback()

finally:
    conn.close()
        
    