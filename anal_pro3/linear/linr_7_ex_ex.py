import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import statsmodels.formula.api as smf
from pandas.tests.frame.test_sort_values_level_as_str import ascending
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import MySQLdb
import ast
from statsmodels.stats.anova import anova_lm

"""
회귀분석 문제 2) 
github.com/pykwon/python에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
"""
ex1 = pd.read_csv("https://raw .githubusercontent.com/pykwon/python/master/testdata_utf8/student.csv")
#print(ex1.head(5))
#print(ex1.corr()) # 0.766263
model = smf.ols(formula = '수학 ~ 국어', data = ex1).fit()
#print(model)
pred = model.predict()
#print("실제값 : ", ex1.국어[:5])
#print("예측값 : ", pred[:5])

kor = float(input('국어 점수를 입력하세요.'))
x_new = pd.DataFrame({'국어' : [kor]})
print("국어 점수로 예측된 수학 점수 :", model.predict(x_new))

model2 = smf.ols(formula = '수학 ~ 국어 + 영어', data = ex1).fit()
#print(model2.summary()) # Durbin-Watson:  2.163
# 국어, 영어 점수 입력하여 수학점수 예측하기
#print(model2.predict())
kor, eng = input("국어 영어 점수를 입력하세요.(띄어쓰기해서 적으시오)").split()
new_data = pd.DataFrame({'국어' : [float(kor)], '영어' : [float(eng)]})
pred2 = model2.predict(new_data)
print('국어,영어 점수로 예측된 수학 점수 결과 : ', pred2)

"""
회귀분석 문제 3) 
원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
"""
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
    sql = '''
        SELECT YEAR(NOW()) - year(jikwon_ibsail) AS years, jikwon_pay FROM jikwon
    '''
   
    df = pd.read_sql(sql,conn)
    #print(df)
    x = df.years
    y = df.jikwon_pay
    model = stats.linregress(x,y)
    #plt.scatter(x,y)
    ndf = float(input("근무년수 입력: "))
    newdf = pd.DataFrame({'years':[ndf]})
    print('연봉: ',np.polyval([model.slope, model.intercept], newdf))
except Exception as e2:
    print('sql err : ' + str(e2))
   
finally:
    cursor.close()
    conn.close()

