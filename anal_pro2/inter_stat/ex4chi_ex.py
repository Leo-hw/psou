'''
카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
  예제파일 : cleanDescriptive.csv
  칼럼 중 level - 부모의 학력수준(대학원1,대졸:2,고졸:3), pass - 자녀의 대학 진학여부(성공:1, 실패:2)
  조건 : NA가 있는 행은 제외한다.
'''

import pandas as pd
import scipy.stats as stats
import MySQLdb
import numpy as np
import ast
import csv


data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/cleanDescriptive.csv')
print(data.head())
data = data.dropna()
print(data.head())
print(data['level'].unique())

# 귀무 : 부모의 학력과 자녀의 진학여부가 관련이 없다.
# 대립 : 부모의 학력과 자녀의 진학여부가 관련이 있다.

ctab = pd.crosstab(index = data['level'], columns = data['pass2'])        # 빈도수
ctab.index=['대학원졸', '대졸', '고졸']
print(ctab)

chi_result = [ctab.loc['대학원졸'], ctab.loc['대졸'], ctab.loc['고졸']]
chi2, p, ddof, expected = stats.chi2_contingency(chi_result)

msg = 'chi2:{}, p-value:{}, df:{}'
print(msg.format(chi2, p, ddof))
print('expected : \n', expected)       
# p-value:0.02029806240489237 < 0.05 이므로 귀무가설 기각

'''
카이제곱 문제2) jikwon_jik과 jikwon_pay 간의 관련성 분석. 가설검정하시오.
  예제파일 : MariaDB의 jikwon table 
  jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
  jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
  조건 : NA가 있는 행은 제외한다.
'''

try :
    with open('mariadb.txt', mode='r') as f:
        config = f.read()
        #print(config)        # class 'str'
    
except Exception as e:
    print('read err :' +str(e))

config = ast.literal_eval(config)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """
    df = pd.read_sql(sql, conn)
    df.columns=['변호', '이름','부서','jikwon_jik','성별','jikwon_pay']
    map_jik = {"이사":1, "부장":2, "과장":3, "대리":4, "사원":5}
    df["jikwon_jik_section"] = df["jikwon_jik"].apply(map_jik.get)
    
    bins = [1000, 3000, 5000, 7000, 10000]
    bins_label = [1, 2, 3, 4]
    df["jikwon_pay_section"] = pd.cut(df['jikwon_pay'], bins, right = False, labels = bins_label)
    # ser.replace([1, 2, 3, 4, np.nan], [6, 7, 8, 9, 10])
    #df.replace({'col1': old_val}, {'col1': new_val})
    #df2['직급'].replace(['이사','부장','과장','대리','사원'], [1,2,3,4,5])
    #df2.replace(({'직급':'이사'},{'직급':1}),({'직급':'부장'},{'직급':2}),({'직급':'과장'},{'직급':3}),({'직급':'대리'},{'직급':4}),({'직급':'사원'},{'직급':5}))
    
    #print(df)
    ctab = pd.crosstab(index = df['jikwon_jik'], columns= df['jikwon_pay_section'])
    print(ctab)
    chi_jik = [ctab.loc['과장'], ctab.loc['대리'], ctab.loc['부장'], ctab.loc['사원'], ctab.loc['이사']]
    chi2, p, ddof, expected = stats.chi2_contingency(chi_jik)        # 이원 카이제곱
    msg = 'chi2:{}, p-value:{}, df:{}'
    print(msg.format(chi2, p, ddof))
    print('expected : \n', expected)      
    
except Exception as e2:
    print('db connection err:' + str(e2))

finally:
    cursor.close()
    conn.close()

