#pip install xgboost

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
import xgboost as xgb

def abcFunc():
    iris = datasets.load_iris()
    print(iris.feature_names)
    print(iris.target_names)
    
    data = pd.DataFrame(
        {
            'sepal length':iris.data[:, 0],
            'sepal width':iris.data[:, 1],
            'petal length':iris.data[:, 2],
            'petal width':iris.data[:, 3],
            'species':iris.target
            }
        )
    print(data.head(3))
    
    x = data[['sepal length', 'sepal width', 'petal length', 'petal width']]
    y = data['species']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    
    # model     :     Bagging 알고리즘
    model = RandomForestClassifier(n_estimators= 100)           # 앙상블 기법/ bagging or boost 
    model.fit(x_train, y_train) 
    
    #predict
    pred1 = model.predict(x_test)
    print('실제 값 : ',np.array(y_test[:5]))
    print('예측 값 : ',pred1[:5])
    print('분류 정확도 : ', metrics.accuracy_score(y_test, pred1))
    
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