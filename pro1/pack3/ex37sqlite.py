#sqlite3: 내장된 개인용 databse

import sqlite3


def dbFunc(dbName):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
#         try:
#             c.execute("select * from jikwon")
#         except:
#             c.execute("create table jikwon(id integer primary key, name text")
        
        c.execute("drop table jikwon")
        c.execute("create table jikwon(id integer primary key, name text)")
        
        # insert
        c.execute("insert into jikwon values(1,'홍길동')")
        
        tdata = (2,'고길동')       #tuple type
        c.execute("insert into jikwon values(?,?)", tdata)
        
        tdata2 = 3, '나길동'            # tuple type
        c.execute("insert into jikwon values(?,?)", tdata2)
        
        tdata3 = ((4,'관우'), (5, '장비'))   # tuple type 여러개 집어넣을 때 executemany
        c.executemany("insert into jikwon values(?,?)", tdata3)
        
        ldata = [6, '조자룡'] # list type
        c.execute("insert into jikwon values(?,?)", ldata)
        
        #sdata = {7, '삼장'} # set type            ----> set type 은 불가능.
        #c.execute("insert into jikwon values(?,?)", sdata)
        
        dicdata1 = {'id':7, 'name':'공기밥'}               # dict type ---> 그냥 넣으면 에러. binding 해야함
        c.execute("insert into jikwon values(:id,:name)", dicdata1)
        
        dicdata2 = {'sabun':8, 'name':'고래밥'}                                                            #dict type 의 경우 column 명을 적는 게 아니라, key 값을 일치 시켜서 넣어주면 됨.
        c.execute("insert into jikwon values(:sabun,:name)", dicdata2)
        
        
        conn.commit()
        
        #select
        print('출력1')
        c.execute("select * from jikwon")
        for r in c:
            print(str(r[0]) + ' ' + r[1])
        
        print('출력2 : 부분 자료')
        c.execute("select * from jikwon where id<=2")
        for r in c.fetchall():
            print(str(r[0]) + ' ' + r[1])
        #bun = 2
        #c.execute("select * from jikwon where id<= %d%bun")
        ir = '홍길동'
        c.execute("select * from jikwon where name='%s'"%ir)
        
        for r in c.fetchall():
            print(str(r[0]) + ' ' + r[1])
            
        print('출력 3: sql 지원함수')
        c.execute("select count(*)from jikwon")
        print(' 건수  : ' + str(c.fetchone()[0]))
        
        
    except Exception as e:
        print('err : ' + e)
        conn.rollback()
    finally:
        conn.close()
        

if __name__ == '__main__':
    dbFunc('test.db')
    
    

