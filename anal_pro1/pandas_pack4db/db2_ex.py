# pandas 문제 5)
# #  MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
# #      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
# #      - 부서명별 연봉의 합, 평균을 출력
# #      - 부서명, 직급으로 교차테이블을 작성(crosstab)
# #      - 직원별 담당 고객자료를 출력
# #      - DataFrame의 자료를 파일로 저장

import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv
import matplotlib.pyplot as plt


try :
    with open('mariadb.txt', mode='r') as f:
        config = f.read()
        #print(config)        # class 'str'
    
except Exception as e:
    print('read err :' +str(e))


try:
    config = ast.literal_eval(config)
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    sql = """
        select jikwon_no, jikwon_name, buser_name,  jikwon_pay, jikwon_jik 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """
    
    df = pd.read_sql(sql, conn)
    df.columns =['사번','이름','부서명','연봉', '직급']
    
    print()
    pdf = pd.DataFrame(df)
    print(pdf.head(3))
    print('-------------------------------------------------------------')
    
    jik_ypay = df.groupby(['부서명'])['연봉'].agg(['sum','mean'])
    print(jik_ypay)
#     jik_apay = df.groupby(['부서명'])['연봉'].mean()
#     jik_spay = df.groupby(['부서명'])['연봉'].sum()
#     print('\n부서별 연봉 합\n', jik_spay,'\n\n부서별 연봉 평균\n', round(jik_apay,2))
    print('교차표 : ', pd.crosstab(df['부서명'], df['직급']))          # html 로 출력 가능 (crosstab, dataframe도 가능 // series 는 안됨.
    print()
    print('-------------------------------------------------------------')
    print()
    sql2 ="""
    select * from jikwon join gogek on jikwon_no = gogek_damsano
    """ 
    
    df2 =  pd.read_sql(sql2, conn)
    pd.set_option('display.max_columns', 500) # 생략 없이 전체 보기.
    print(df2.groupby(['jikwon_name'])['gogek_name'].count())
    print('*************************************************************************************')
    #print(df2.pivot_table(df2, index=['jikwon_name']))
    
    
        
except Exception as e:
    print('sql err : ' + str(e))

finally:
    cursor.close()
    conn.close()
    