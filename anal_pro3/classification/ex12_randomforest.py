# 앙상블 기법 중 Bagging 알고리즘에 의사결정나무 트리를 여러개 사용하여 하나의 샘플 데이터에 다양한 변화를 주면서 최종 결과를 만들어 나가는 분류기


# 타이타닉 데이터로 연습
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import model_selection 

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df.head(), ' ', df.shape)     # (891, 12)
print(df.info())
df = df.dropna(subset=['Pclass', 'Age', 'Sex'])
print(df.shape)

df_x = df[['Pclass', 'Age', 'Sex']]
print(df_x, type(df_x))


# Scaling ---------------------
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df_x.loc[:, 'Sex'] = LabelEncoder().fit_transform(df_x['Sex'])          # male : 1, female : 0
#df_x['Sex'] = df_x['Sex'].apply(lambda x:1 if x == 'male' else 0)        위와 동일함. 람다식 사용.
print(df_x.head())

import numpy as np
df_x2 = pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:, np.newaxis]).toarray(), 
                     columns = ['f_class','s_class','t_class'], index = df_x.index)


#print(df_x2)
df_x = pd.concat([df_x, df_x2], axis = 1)
print(df_x.head(3))
df_y = df['Survived']
print(df_y.head(3))
# train / test 로 분리
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size = 0.3, random_state = 12)
print(train_x.shape, test_x.shape)  #(499, 6) (215, 6)

#model 사용
model = RandomForestClassifier(n_estimators=1500, criterion = 'entropy')     # estimator 의사 결정 나무의 갯수
fitted_model = model.fit(train_x, train_y)

pred = fitted_model.predict(test_x)
print('예측 값 : ', pred[:5])
print('실제 값 : ', np.array(test_y[:5]))

# 정확도
print('acc :  ', sum(test_y == pred) / len(test_y))

from sklearn.metrics import accuracy_score
print('acc :  ', accuracy_score(test_y,  pred))

# 교차 검증
cross_vali = model_selection.cross_val_score(model, df_x, df_y, cv = 5)
#print(cross_vali)       # [0.76923077 0.81818182 0.81818182 0.83216783 0.83802817]
print(np.round(np.mean(cross_vali), 3))