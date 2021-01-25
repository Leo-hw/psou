# 원격 DBMS 와 연동 : Maria Db

import MySQLdb
# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close

# 연결 정보를 dict type 으로 저장
config = {                       
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    #print(conn)
    cursor = conn.cursor()
    
    # 자료 추가
    #sql = "insert into sangdata(code, sang, su, dan) values(20, '신상1', 5, 50000)"
    #cursor.execute(sql)
    '''
    sql = "insert into sangdata(code, sang, su, dan) values(%s, %s, %s, %s)"
    #sql_data = ('21', '신상2', 10,2500)
    sql_data = 21, '신상2', 10,2500
    result = cursor.execute(sql,sql_data)
    print('result : ', result)
    conn.commit()
    '''
    
    # 자료 수정
    '''
    sql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s"
    sql_data = ('마스크', 100, 70000, 21)
    result = cursor.execute(sql,sql_data)
    print('수정 result : ', result)
    conn.commit()
    '''
    
    #자료 삭제
#     code = 21
#     sql = "delete from sangdata where code =" + code             ----> 이렇게도 사용가능 #비권장
    
    #code = 21                                                                                                                       #권장1
    #sql = "delete from sangdata where code =%s"
    #cursor.execute(sql, (code,))    
    
    code = 21                                                                                                                       #권장2
    sql = "delete from sangdata where code ='{}'".format(code)
    res  = cursor.execute(sql)
    print('삭제 res:' ,res)
    conn.commit()
    
    print('-----------자료 읽기-------------')
    sql = "select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    #방법1
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
        
    print()
    
     #방법2
    for r in cursor:
        print(r[0], r[1], r[2],r[3])
        
    print()
    #방법3
    for (code, sang, su, dan) in cursor:                    # 여기 들어가는 건 컬럼 명이 아니라 변수와 1:1 매핑 하는 것이므로, 변수와 매핑만 제대로 해주면 됨.
        print(code, sang, su, dan)
    
    print()
    
    #방법3 - 1
    for (a, b, 수량, 단가) in cursor:
        print(a, b, 수량, 단가)
        
    
except Exception as e:
    print('err: '  + e)
    
finally:
    cursor.close()
    conn.close()
    