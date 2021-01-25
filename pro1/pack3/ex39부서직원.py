'''
키보드로 부서번호 입력받아 부서별 직원 출력
'''
config = {                       
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

import MySQLdb
import sys

try:
    conn = MySQLdb.connect(**config)
    #print(conn)
    cursor = conn.cursor()
    
    buser = input('부서 번호 입력 : ')
    sql = '''
            select jikwon_no, jikwon_name, buser_num, jikwon_jik from jikwon
            where buser_num = {0}
    '''.format(buser)
    #print(sql)
    cursor.execute(sql)
    datas = cursor.fetchall()
    
    if len(datas) == 0:
        print(buser + '번 부서는 없는 번호입니다.')
        sys.exit()
    
    for d in datas:
        print(d[0],d[1],d[2],d[3])
    
    
    print('인원 수  : ' + str(len(datas)))
    
    
    
except Exception as e:
    print('err: '  + e)
    
finally:
    cursor.close()
    conn.close()
    
    