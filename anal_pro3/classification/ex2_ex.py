import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

fdata = pd.read_csv('ex2_model.txt')
data = fdata.loc[(fdata['요일'] == '토') | (fdata['요일'] == '일')]
print(data.head(3))

model = smf.glm(formula='외식유무 ~ 소득수준', data = data, family=sm.families.Binomial()).fit()
print(model.summary())
print()
pred = model.predict(data)
print('분류 정확도 : ', accuracy_score(data['외식유무'], np.around(pred)))  # 0.9047619047619048

new_input_data = pd.DataFrame({'소득수준':[int(input('소득수준 : '))]})
print('외식 유무 :', np.rint(model.predict(new_input_data)))
print('외식을 함' if np.rint(model.predict(new_input_data))[0] == 1 else '외식안함')