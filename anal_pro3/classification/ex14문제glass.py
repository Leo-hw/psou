import pandas as pd
import numpy as np
from sklearn.model_selection._split import train_test_split
from sklearn import metrics
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
plt.rc('font', family="malgun gothic")

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/glass.csv")
print(data.columns)
print(data.info())

# pre-processing
x = data.drop('Type', axis=1)  # Type 열은 독립변수에서 제외
y = data['Type']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
print()

# 스케일링
sc = StandardScaler()
sc.fit(x_train, x_test)    # x값만 대상
x_train = sc.transform(x_train)  
x_test = sc.transform(x_test)  

print()
# 중요변수 확인을 위해 위한 RandomForestClassifier 모델 작성
rf_model = RandomForestClassifier(n_estimators=10,criterion="entropy",n_jobs=5,random_state=96)
rf_model.fit(x_train,y_train)

col = pd.DataFrame(x_train,columns=x.columns)
print('col.columns : ', col.columns)

# 변수 중요도 표시 ---------------------------------------------------
varDic = {'var':col.columns,'imp': rf_model.feature_importances_}
imp = pd.DataFrame(varDic)
imp = imp.sort_values(by='imp', ascending=False)[0:17]
print('중요변수 보기 :', imp)  

# 중요변수 시각화 : barChart
importances = rf_model.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf_model.estimators_], axis=0)
indices = np.argsort(importances)[::-1]

plt.title("특성 중요도")
plt.bar(range(x_train.shape[1]), importances[indices],
        color="g", yerr=std[indices], align="center")

x_train = pd.DataFrame(x_train)
plt.xticks(np.arange(x_train.shape[1]), tuple(imp["var"]))
plt.xlim([-1, x_train.shape[1]])
plt.show()


pred = rf_model.predict(x_test)
acc = metrics.accuracy_score(y_test,pred)
print("정확도:", acc)  # 그냥 RandomForestClassifier 모델로도 한번 찍어봄 

print()
print('XGBClassifier model 사용---')
x = data[['Na', 'Al', 'Mg','RI','Ca','Si','K']]
y = data['Type']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
model = xgb.XGBClassifier(booster='gbtree', max_depth=4, n_estimators=1000)
model.fit(x_train,y_train)
print()  
y_pred = model.predict(x_test)  # 예측
print('실제값 :', y_pred[:5])
print('예측값:', np.array(y_test[:5]))
print('정확도 :', metrics.accuracy_score(y_test, y_pred))

