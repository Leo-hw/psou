from django.shortcuts import render
import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv
from myapp.models import Jikwon, Buser
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date
plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지
plt.style.use('ggplot')
# Create your views here.
'''
1) 사번, 직원명, 부서명, 직급, 근무년수, 연봉을 DataFrame에 기억 후 출력하시오.
       : 부서번호, 직원명 순으로 오름 차순 정렬 
   2) 부서명, 직급 자료를 이용하여  각각 급여합, 급여평균을 구하시오.
   3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
   4) 성별, 직급별 빈도표를 출력하시오.
'''


def MainFunc(request):
    return render(request, 'index.html')

def ListFunc(request):
#     try :
#         with open('mariadb.txt', mode='r') as f:
#             config = f.read()
#             print(config)
#         
#     except Exception as e:
#         print('read err :' +str(e))
#     
#     config = ast.literal_eval(config)
#     try :
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()
#         sql = """
#             select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay 
#             from jikwon inner join buser
#             on buser.buser_no = jikwon.buser_num
#         """
#         cursor.execute(sql)
#         for (a,b,c,d,e,f) in cursor:
#             print(a,b,c,d,e,f)
#     
#         df2 = pd.read_sql(sql, conn)
#         df2.columns=['변호', '이름','부서','직급','성별','연봉']
#         print(df2.head(3))
#     
#     
#     except Exception as e2:
#         print('sql err : ' + str(e2))
#     
#     finally:
#         cursor.close()
#         conn.close()
#         
#         
    bdata = Jikwon.objects.all()
    
    #print(sdata)
    datas = []
    for s in bdata:
        
        if s.buser_num == 10:
            buser_name='총무부'
        elif s.buser_num == 20:
            buser_name='영업부'
        elif s.buser_num == 30:
            buser_name='전산부'
        elif s.buser_num == 40:
            buser_name='관리부'

# a = '20160228'
# date = datetime.strptime(a, '%Y%m%d').strftime('%m/%d/%Y')
        dic = {'jikwon_no': s.jikwon_no, 'jikwon_name':s.jikwon_name,  'buser_name' :buser_name, 'jikwon_jik': s.jikwon_jik, 'jikwon_ibsail': date.today()- s.jikwon_ibsail, 'jikwon_pay': s.jikwon_pay}
        datas.append(dic)
             
    
    #print(sdata)
    print(bdata)
    #df = pd.DataFrame(bdata)
    
    df = pd.DataFrame(datas)
    print(type(df['jikwon_ibsail'][0]))
    # 피벗 테이블을 이용해 부서별, 직급별 연봉 평균 구하기.
    pdf = df.pivot_table(['jikwon_pay'], index=['buser_name', 'jikwon_jik'], aggfunc=['sum','mean'])
    # 이렇게 할 경우 연봉 합을 추가 하는 방법?
    
#     adf = df.groupby(['jikwon_jik'])['jikwon_pay'].mean()
#     sdf = df.groupby(['jikwon_jik'])['jikwon_pay'].sum()
#     print(adf)
#     print(sdf)
    '''
    data = {'city':['강남','강북','강남','강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }

    '''
    #data = {'jikwon_apay':adf, 'jikwon_spay':sdf}
    #pdf = pd.DataFrame(data)
    #print(adf)
    #pdf = pd.DataFrame(adf )
    
    #pdf = pd.DataFrame(adf, index=['jikwon_jik'],columns=['연봉 평균','연봉 합'])
    
    #pdf.append(adf)
    #pdf.append(sdf)
    pdf.columns = ['jikwon_apay', 'jikwon_spay']
    
    print(pdf, ' ', type(pdf))
    
#     pdf = pd.DataFrame()
#     pdf.append(adf)
#     pdf.append(sdf)
     
    gdf = df.to_html()
    pdff = pdf.to_html()
    
    #print(pdf['jikwon_apay'])
    plt.rc('font', family = 'malgun gothic')
    
    # 여기서 그래프 그려서 그런가...?(다른 펑션에서 해야하남...)
    #titanic = sns.load_dataset('titanic')             # seaborn 이 제공하는 dataset  의 일종
    
    
    
#     ggdata = [50,80,100,70,90]
#     plt.bar(range(len(ggdata)), ggdata)
#     plt.show()
    #sns.barplot(x ='jikwon_apay',data=pdf)
    #plt.bar(range(len(pdf)), pdf)
    #plt.show()
#     figure,ax = plt.subplots(nrows=1, ncols=4)
#     figure.set_size_inches(15, 5)       # 크기 변경
#     sns.barplot(data=pdf)

    
    #sns.countplot(x="buser_name", data=pdf)
    #plt.title("타이타닉호의 각 클래스별, 승객 수")
    
    
    #plt.show()

    
    
#     print(len(jik_ypay))
#     
#     plt.bar(jik_ypay,
#              labels = jik_ypay.index
#              )
#     #plt.bar(len(jik_ypay),jik_ypay)
#     plt.show()
    
    return render(request, 'list.html', {'gdf':gdf,'pdf':pdff })
