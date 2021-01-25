import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
import MySQLdb
import ast
'''
[ANOVA 예제 1]
빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

'''

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.

kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, None, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33,  44,  55, 66,  77]

# print(len(kind), len(quantity))
data = pd.DataFrame([kind,quantity]).T
data.columns = 'kind', 'quantity'
data = data.fillna(data['quantity'].mean()) # None 값 제외하고 합치고 나눈 값
data = data.astype({'kind':int})
# print(data)

oil1 = data[data['kind']==1]
oil2 = data[data['kind']==2]
oil3 = data[data['kind']==3]
oil4 = data[data['kind']==4]

suck_oil1 = oil1['quantity']
suck_oil2 = oil2['quantity']
suck_oil3 = oil3['quantity']
suck_oil4 = oil4['quantity']

print('\n등분산성')
print('levene :', stats.levene(suck_oil1, suck_oil2, suck_oil3, suck_oil4).pvalue)
print('fligner :', stats.fligner(suck_oil1, suck_oil2, suck_oil3, suck_oil4).pvalue)
print('bartlett :', stats.bartlett(suck_oil1, suck_oil2, suck_oil3, suck_oil4).pvalue)
# 등분산성 만족

print('\n정규성')
print(stats.shapiro(suck_oil1))
print(stats.shapiro(suck_oil2))
print(stats.shapiro(suck_oil3))
print(stats.shapiro(suck_oil4))
# 정규성 만족

print('\nANOVA')
regModel = ols('data["quantity"] ~ C(data["kind"])', data=data).fit() 
table = anova_lm(regModel, type=1)
print(table) 
# p-value=0.848244 > 0.05 귀무가설 채택.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.

print('----' * 20)

'''
[ANOVA 예제 2]
DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
'''
# 귀무 : 부서별 연봉에 차이가 없다.

try:
    with open('mariadb.txt', mode='r') as f:
        config = f.read()
except Exception as e:
    print('read err : ' + str(e))
    
config = ast.literal_eval(config)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name, jikwon_pay from jikwon 
        left outer join buser on buser_num = buser_no
    """
    cursor.execute(sql)
    df = pd.read_sql(sql, conn)
    print(df.head())
    
    buser1 = df[df['buser_name'] == '총무부']  # 총무부    
    buser2 = df[df['buser_name'] == '영업부']  # 영업부
    buser3 = df[df['buser_name'] == '전산부']  # 전산부
    buser4 = df[df['buser_name'] == '관리부']  # 관리부
    
    b1pay = buser1['jikwon_pay']
    b2pay = buser2['jikwon_pay']
    b3pay = buser3['jikwon_pay']
    b4pay = buser4['jikwon_pay']
    
    
    print('\n등분산성')
    print('levene :', stats.levene(b1pay, b2pay, b3pay, b4pay).pvalue)
    print('fligner :', stats.fligner(b1pay, b2pay, b3pay, b4pay).pvalue)
    print('bartlett :', stats.bartlett(b1pay, b2pay, b3pay, b4pay).pvalue)
    # p_val : 0.9 > 0.05 등분산성 만족
    
    print('\n정규성')
    print(stats.shapiro(b1pay).pvalue)
    print(stats.shapiro(b2pay).pvalue)
    print(stats.shapiro(b3pay).pvalue)
    print(stats.shapiro(b4pay).pvalue)
    # 정규성 만족 x
    
    print('\nkruscal-wallis test')
    print(stats.kruskal(b1pay, b2pay, b3pay, b4pay).pvalue)
    # p_val = 0.8506424005016474 > 0.05 귀무 채택
    # 부서별 연봉에 차이가 없다.

except Exception as e:
    print(e)
    
finally:
    cursor.close()
    conn.close()

