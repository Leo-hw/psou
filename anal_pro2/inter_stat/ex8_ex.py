import pandas as pd
from scipy import stats
from numpy import average
import ast
import csv
import MySQLdb




# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
print('----------------------------문제1-------------------------------------------------')
blue =[70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80] 
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66] 

print('blue : ', average(blue))#blue :  72.81818181818181
print('red : ', average(red))#red :  63.81818181818182

print(average(blue) - average(red)) #8.999999999999993 차이 날 확률?

# 귀무 가설 : 포장지 색상에 따른 매출액의 차이가 없다.
# 대립 가설 : 포장지 색상에 따른 매출액의 차이가 있다.

print(' blue 정규성:', stats.shapiro(blue))
print(' red 정규성:', stats.shapiro(red))
print(stats.wilcoxon(blue, red, mode='approx'))
# 선행 조건 : 1, 정규성, 2 등분산성
two_sample = stats.ttest_ind(blue, red)
two_sample = stats.ttest_ind(blue, red, equal_var = True) # (default) 정규분포의 분산을 같다.
print(two_sample)   # Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784402)
# 해석 : p (0.0083) < a (0.05) -> 귀무가설 기각.( 포장지 색상에 따른 차이가 존재)

print('----------------------------문제2-------------------------------------------------')
# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
#   남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
#   여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]


print('male:', average(male)) # male: 3.0652173913043472
print('female:', average(female)) #female: 3.54
# 귀무 가설 : 차이가 없다.
# 대립 가설 : 차이가 있다. 
print(' 정규성:', stats.shapiro(male))
print(' 정규성:', stats.shapiro(female))
print(stats.wilcoxon(male))
print(stats.wilcoxon(female))
print(stats.mannwhitneyu(male, female))
two_sample = stats.ttest_ind(male, female)
two_sample = stats.ttest_ind(male, female, equal_var = True) # (default) 정규분포의 분산을 같다.
print(two_sample) # Ttest_indResult(statistic=-0.7114720893202576, pvalue=0.48082034441892807)
#해석 pvalue=0.48 > 0.05 이므로 귀무가설 채택 ( 혈관내 콜레스테롤 양에 차이가 없다.)

print('----------------------------문제3-------------------------------------------------')
# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
# 귀무가설 : 연봉에 차이가 없다.
# 대립가설 : 연봉에 차이가 있다.

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
    sql1 = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num where buser_name = '총무부'
    """
    sql2 = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num where buser_name = '영업부'
    """
    df1 = pd.read_sql(sql1, conn)
    df2 = pd.read_sql(sql2, conn)
#     print(df1)
#     print(df2)
    print('총무부 연봉평균', average(df1['jikwon_pay']))
    print('영업부 연봉평균', average(df2['jikwon_pay']))
    print(' df1 정규성:', stats.shapiro(df1['jikwon_pay']))
    print(' df2 정규성:', stats.shapiro(df2['jikwon_pay']))
    print(stats.wilcoxon(df1['jikwon_pay']))
    print(stats.wilcoxon(df2['jikwon_pay']))
    print(stats.mannwhitneyu(df1['jikwon_pay'], df2['jikwon_pay']))
    two_sample = stats.ttest_ind(df1['jikwon_pay'], df2['jikwon_pay'])
    two_sample = stats.ttest_ind(df1['jikwon_pay'], df2['jikwon_pay'], equal_var = True)
    print(two_sample) # Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
    # pvalue= 0.23 > 0.05 이므로 귀무가설 채택
        

except Exception as e2:
    print('sql err : ' + str(e2))
    
finally:
    cursor.close()
    conn.close()
print('----------------------------문제4-------------------------------------------------')
# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다.
# 점수는 학생 번호 순으로 배열되어 있다.
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

med = [ 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80] 
fin = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

#  귀무가설 : 변화가 없다.
# 대립 가설 : 변화가 았다.
print('중간 평균 : ', average(med)) #74.16666666666667
print('기말 평균 : ', average(fin)) #81.66666666666667

print('등분산성(levene)', stats.levene(med, fin)) # 모수 검정 (가장 많이 쓰임)
#등분산성(levene) LeveneResult(statistic=0.5657142857142856, pvalue=0.45993912889208344)

two_sample = stats.ttest_rel(med, fin)
print(stats.wilcoxon(med, fin)) 
print(two_sample)   # Ttest_indResult(statistic=-1.3695946384548277, pvalue=0.1846323128864873)
# pvalue = 0.023 < 0.05 이므로 귀무가설 기각.
