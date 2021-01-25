# 원격 DB 연동 후 테이블 자료 읽어 DataFrame 으로 객체화
import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv


try :
    with open('mariadb.txt', mode='r') as f:
        config = f.read()
        #print(config)        # class 'str'
    
except Exception as e:
    print('read err :' +str(e))





config = ast.literal_eval(config)
try :
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """
    cursor.execute(sql)
    for (a,b,c,d,e,f) in cursor:
        print(a,b,c,d,e,f)
    '''
    # table 의 자료를 csv 파일로 저장
    with open('jik_data.csv', 'w', encoding='utf-8') as fw:
        writer = csv.writer(fw)
        for row in cursor:
            writer.writerow(row)
        print('저장완료')
    '''
    # 읽기1,  csv 파일 -> dataFrame
    df1 = pd.read_csv('jik_data.csv', header=None, names=('변호', '이름','부서','직급','성별','연봉'))
    print(df1.head(3))
    print()
    
    #읽기 2, sql문 -> DataFrame
    df2 = pd.read_sql(sql, conn)
    df2.columns=['변호', '이름','부서','직급','성별','연봉']
    print(df2.head(3))
    
    print('전체 인원수 : ', len(df2), df2['이름'].count(), df2['직급'].count())
    print('직급별 인원수 : ', df2['직급'].value_counts())
    print('부서별 인원수 : ', df2['부서'].value_counts())
    
    print('연봉 평균 : ' , df2.loc[:, '연봉'].sum()/len(df2))
    print('연봉 평균 : ', df2.loc[:, ['연봉']].mean())
    print('연봉 요약 통계량 : ', df2.loc[:, ['연봉']].describe())
    print('연봉이 5000 이상 : ', df2.loc[df2['연봉']>= 7000] )
    print('연봉이  5000 이상 영업부 : ', df2.loc[(df2['연봉']>= 5000) &( df2['부서'] == '영업부')])
    print('교차표 : ', pd.crosstab(df2['성별'], df2['직급']))          # html 로 출력 가능 (crosstab, dataframe도 가능 // series 는 안됨.
    print()
    
    # 그룹화
    print(df2.groupby(['성별'])['이름'].count())            #성별 인원수
    print(df2.groupby(['성별','직급'])['이름'].count())           # 성별/직급별 인원수
    
    # pivot table : 성별 내의 직급별 연봉 평균
    print(df2.pivot_table(['연봉'], index=['성별', '직급'], aggfunc=np.mean))
    
    # 시각화
    import matplotlib.pyplot as plt
    plt.rc('font', family = 'malgun gothic')
    
    jik_ypay = df2.groupby(['직급'])['연봉'].mean()
    print(jik_ypay.index)
    print(jik_ypay.values)
    
    plt.pie(jik_ypay, labels = jik_ypay.index, 
            labeldistance=0.5, 
            counterclock=False,
            explode=(0.2, 0,0,0.3,0),
            shadow=True
            )
    plt.show()
    
    
    

    
    
except Exception as e2:
    print('sql err : ' + str(e2))
    
finally:
    cursor.close()
    conn.close()