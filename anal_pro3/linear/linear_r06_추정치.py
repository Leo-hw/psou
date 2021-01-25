# mtcars dataset을 이용해 연비 추정 선형 회귀 모델 작성 후 처리
import statsmodels.api
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
# pd.set_option('display.max_columns', 500) # 펼쳐 보기
print(mtcars.head())
print(mtcars.info()) # mpg: 연비, hp: 마력수
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # -0.77616837 (매우 강한 음의 상관 관계)
# 마력이 증가하면 연비가 떨어진다.

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1) # polyfit: model 없이 회귀선을 보여줌, 1: 1차식(직선)
# plt.plot(mtcars.hp, slope * mtcars.hp + intercept, 'b') # x, y, color
# plt.show()
print()

print('단일 선형회귀 분석 --------------')
result = smf.ols(formula = 'mpg ~ hp', data = mtcars).fit()

print(result.conf_int(alpha = 0.05)) # (default) alpha = 0.05 (= 95% confidence interval)
'''                0          1
Intercept  26.761949  33.435772
hp         -0.088895  -0.047562'''

print(result.conf_int(alpha = 0.01))
'''                0          1
Intercept  25.605585  34.592136
hp         -0.096056  -0.040400'''

# print(result.summary()) → 사실 배열 형태임
print(result.summary().tables[1])
'''===========================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     30.0989      1.634     18.421      0.000      26.762      33.436
hp            -0.0682      0.010     -6.742      0.000      -0.089      -0.048
==========================================================================='''
print(result.rsquared) # 결정 계수: 0.602437341423934
# print(result.predict())

print('다중 선형회귀 분석 --------------')
result2 = smf.ols(formula = 'mpg ~ hp + wt', data=mtcars).fit() # wt: 차 무게
print(result2.summary())
print()


print('추정치 구하기--------------')
result3 = smf.ols(formula = 'mpg ~ wt', data=mtcars).fit() # wt: 차 무게
print(result3.summary().tables[1])
print('결정계수:', result3.rsquared) # 0.7528327936582646 (강한 설명력)

kbs = result3.predict()
# print(kbs) # 모든 wt에 대한 예측값
print('실제값:', mtcars.mpg[:3])
print('예측값:', kbs[:3])

# 전체 자료 실제값, 예측값 비교
data = {
    'mpg': mtcars.mpg,
    'predict': kbs
}
df = pd.DataFrame(data)
print(df)
print()

# 임의의 차체 무게에 대한 연비 확인
mtcars.wt = 6 # 차체 무게가 6t이면 연비는?
ytn = result3.predict(pd.DataFrame(mtcars.wt))
print(ytn[0]) # 5.218296731005985
print()

mtcars.wt = 0.5 # 차체 무게가 500kg이면 연비는?
ytn = result3.predict(pd.DataFrame(mtcars.wt))
print(ytn[0]) # 34.6128903809807 (반비례 관계)
print()

## 복수개 독립변수 입력
wt_new = pd.DataFrame({'wt':[2, 3.5, 4.2, 0.3]})
preds = result3.predict(wt_new)
print(preds)
'''
0    26.596183
1    18.579476
2    14.838346
3    35.681785
dtype: float64'''
# 예측값에 반올림 (np.round())
print(np.round(preds.values, 3)) # [26.596 18.579 14.838 35.682]

