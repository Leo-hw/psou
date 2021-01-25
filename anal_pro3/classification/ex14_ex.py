'''
[XGBoost 문제] 
kaggle.com이 제공하는 'glass datasets'
유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    type
glass.csv 파일을 읽어 분류 작업을 수행하시오.
'''
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
import xgboost as xgb
from sklearn.preprocessing._data import StandardScaler

# https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/glass.csv

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/glass.csv')
print(data.head())

def abcFunc():
    # 전처리
    x = data[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
    y = data['Type']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
    
    #스케일링
    sc = StandardScaler()
    sc.fit(x_train, x_test)    # x값만 대상
    x_train = sc.transform(x_train)  
    x_test = sc.transform(x_test)  
    
    
    # model2     :     Boosting 알고리즘 (성능은 더 우수하나, overfitting(과적합) 의 우려)  - kaggle 에서는 XGBooster 가 더 많이 쓰임.
    model2 = xgb.XGBClassifier(booster='gbtree', max_depth = 4)        #gbtree 는 의사결정, linear 도 가능.
    model2.fit(x_train, y_train) 
    #predict
    pred2 = model2.predict(x_test)
    print('실제 값 : ',np.array(y_test[:5]))
    print('예측 값 : ',pred2[:5])
    print('분류 정확도 : ', metrics.accuracy_score(y_test, pred2))
    
if __name__ == '__main__':
    abcFunc()