# 로지스틱 회귀분석 (Logistic Regression)  : 선형 회귀 분석 확장 개념
# 독립변수 : 연속형,   종속변수 : 범주형
# odds -> odds ration -> lgoit function -> sigmoid function (범위를 양의 무한대, 음의 무한대에서 시그모이드 함수를 이용해 0~1 사이로 조정)

# sigmoid function test
import math

def sigmoidFunc(x):
    return 1 / (1+ math.exp(-x))

print(sigmoidFunc(3))
print(sigmoidFunc(-3))
print(sigmoidFunc(1))
print(sigmoidFunc(-5))


print('------------------------------')
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np

mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))


mtcar = mtcars.loc[:, ['mpg','hp','am']]
print(mtcar.head(2), ' ', mtcar['am'].unique())     # [1 0]

# 방법 1 logit()
formula = 'am ~ hp + mpg'
result = smf.logit(formula=formula, data = mtcar).fit()
print(result)
print(result.summary())

#print('예측값 : ', result.predict())
pred = result.predict(mtcar[:5])
print('예측값: ', np.around(pred))
print('실제값: ', mtcar['am'][:5])

print()
conf_tab = result.pred_table()
print('confusion matrix:\n', conf_tab)

# 분류 정확도
print('분류 정확도 : ' , (16+10)/len(mtcar))     # 분류 정확도 :  0.8125
print('분류 정확도 : ' , (conf_tab[0][0]+conf_tab[1][1])/len(mtcar)) #분류 정확도 :  0.8125
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('분류 정확도 : ', accuracy_score(mtcar['am'],np.around(pred2 )))
print('***' * 10)
# 방법 2 glm()
result2 = smf.glm(formula = formula, data = mtcar, family=sm.families.Binomial()).fit()
print(result2)
print(result2.summary())
glm_pred = result2.predict(mtcar[:5])
print('glm_pred : ', np.around(glm_pred))

glm_pred2 = result2.predict(mtcar)
print('분류정확도2:', accuracy_score(mtcar['am'], np.around(glm_pred2)))

print('\n 새로운 값으로 예측 결과를 얻기')
newdf =mtcar.iloc[:2].copy()
print(newdf)
newdf['mpg'] = [10,35]
newdf['hp'] = [80, 150]
print(newdf)
glm_pred_new  = result2.predict(newdf)
print('glm_pred_new : ' , np.around(glm_pred_new))
print('glm_pred_new : ' , np.rint(glm_pred_new))


print()
import pandas as pd
newdf2 = pd.DataFrame({'mpg':[10, 100], 'hp':[200, 200]})
glm_pred_new2  = result2.predict(newdf2)
print('glm_pred_new : ' , np.around(glm_pred_new2))
print('glm_pred_new : ' , np.rint(glm_pred_new2))


