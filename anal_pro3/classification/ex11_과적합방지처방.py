# 과적합 (Overfitting) : 학습데이터에 모델이 최적화되면 실제 데이터에 대한 분류 예측의 정확도가 떨어질 수 있다.
# 과적합 방지를 위한 작업  -  train_test_split, K-fold ...
# 포용성이 있는 모델을 만드는 것이 목적.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
print(iris.keys())

train_data = iris.data
train_label = iris.target
print(train_data[:3])
print(train_label[:3])

# 분류 모델 사용
dt_clf = DecisionTreeClassifier()           # 다른 모델도 가능.(ex, random forest, knn ...
dt_clf.fit(train_data, train_label)
pred = dt_clf.predict(train_data)
print('예측 값 : ',pred)
print('실제 값: ',train_label)
print('분류 정확도  : ', accuracy_score(train_label, pred))      # 분류 정확도 : 1.0
# 이 모델의 성능이 100% 이지만 겁나 찝찝!!(train data 만 사용) - train 으로 학습 train 으로 테스트
# 과적합 문제 발생. 새로운 데이터에 대해 분류 성능을 믿을 수 없음.

print('\n과적합 방지 목적의 처리 방법 1 ---------------------------------') 
# train_test_split 일반적으로 7:3. 데이터의 양이 충분할 경우.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=121)
dt_clf.fit(x_train, y_train)
pred2 = dt_clf.predict(x_test)
print('예측 값 : ',pred2)
print('실제 값: ',y_test)
print('분류 정확도  : ', accuracy_score(y_test, pred2))      # 0.955 추론 통계는 모든 환경에 100%가 될 수는 없다.

print('\n 과적합 방지 목적의 처리 방법2 =================')
# 교차 검증 : train_test_split 에서도 과적합 발생할 가능성 있다. 또는 데이터 양이 적을 경우,
# 데이터 편중을 방지하고자 학습데이터(train data) 를 분리해 학습과 평가를 병행하는 방법
# 가장 보편적인 방법 : K-fold 교차 검증, validation data 를 사용.
from sklearn.model_selection import KFold
import numpy as np
features = iris.data
label = iris.target

dt_clf = DecisionTreeClassifier(random_state = 123)
kfold = KFold(n_splits=5)
cv_acc = []
print('iris shape : ', features.shape, 4/5*150)     # (150,4) 학습데이터 120개, 검증데이터 : 30 개로 분할해서 모델을 학습.

n_iter = 0
for train_index, test_index in kfold.split(features):
    '''
    print('n_iter: ', n_iter)
    print(train_index, ' ', len(train_index))
    print(test_index, ' ', len(test_index))
    n_iter += 1
    '''
    # kfold.split() 변환된 인덱스를 이용해 train, test 데이터 추출
    xtrain, xtest = features[train_index],features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)  
    n_iter += 1
    # 반복할 때마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0},     교차 검증 정확도 :  {1},    학습데이터 크기 : {2},     검정데이터 크기 : {3}'. format(n_iter, acc, train_size, test_size))
    print('반복수 : {0},    testset : {1}'.format(n_iter, test_index))
    cv_acc.append(acc)
    
print('평균 검증 정확도 : ', np.mean(cv_acc))          # k회 교차 검증 결과 평균 :  0.9199999999999999
    
print('\n 과적합 방지 목적의 처리방법2_1 ===========================================================================')
# StratifiedKFold : 불균등한 분포를 가진 레이블(데이터의 분포가 편중) 데이터 집합을 위한 K - fold 방법
from sklearn.model_selection import StratifiedKFold

skfold  = StratifiedKFold(n_splits = 3)
cv_acc=[]
n_iter = 0

for train_index, test_index in skfold.split(features, label):
    # kfold.split() 변환된 인덱스를 이용해 train, test 데이터 추출
    xtrain, xtest = features[train_index],features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)  
    n_iter += 1
    # 반복할 때마다 정확도 측정
    accuracy = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0},     교차 검증 정확도 :  {1},    학습데이터 크기 : {2},     검정데이터 크기 : {3}'. format(n_iter, accuracy, train_size, test_size))
    print('반복수 : {0},    testset : {1}'.format(n_iter, test_index))
    cv_acc.append(accuracy)

print('StratifiedKFold 평균 검증 정확도 : ', np.mean(cv_acc))          # k회 교차 검증 평균 검증 정확도 :  0.9666666666666667


print('\n 과적합 방지 목적의 처리방법2_2 ===========================================================================')
#
from sklearn.model_selection import cross_val_score     # K-fold 를 메소드로 제공
data = iris.data
label = iris.target

score = cross_val_score(dt_clf, data, label, scoring = 'accuracy', cv = 5)
print('교차 검증 별 정확도 : ', np.around(score, 3))
print('평균 검증 정확도 : ', np.around(np.mean(score), 3))

print('\n 과적합 방지 목적의 처리방법3 ===========================================================================')
#최적의 파라미터 값으 ㄹ얻는건데요
#GridSearchCV : 교차 검증과 최적의 파라미터 튜닝을 한번에 처리하는 방법
from sklearn.model_selection import GridSearchCV
# max_depth, min_samples_split 최적화를 진행하여 가장 효과적인 parameter 값 얻기
parameters = {'max_depth':[1,2,3], 'min_samples_split':[2,3]}

grid_dtree = GridSearchCV(dt_clf, param_grid = parameters, cv=3, refit = True)      # refit = True -> 재학습
#grid_dtree : 평가판 모델.(estimator)
grid_dtree.fit(x_train, y_train)             #  자동으로 평가판 모델 객체를 수행해서 내부 모형을 생성. 이를 모두 실행시켜 hyper parameter 반환

# GridSearchCV의 결과를 DataFrame에 저장
import pandas as pd
scores_df = pd.DataFrame(grid_dtree.cv_results_)     #best_score_, best_parameters_ ...
print(scores_df)
print('GridSearchCV  최적의 파라미터 : ', grid_dtree.best_params_)     #{'max_depth': 3, 'min_samples_split': 2}
print('GridSearchCV  최적의 정확도 : ', grid_dtree.best_score_)       #  0.9428571428571427
estimatorModel = grid_dtree.best_estimator_
print(estimatorModel)       # DecisionTreeClassifier(max_depth=3, random_state=123)

pred = estimatorModel.predict(x_test)
print(pred)
print('테스트 데이터로 검증된 정확도 : ', accuracy_score(y_test, pred))  #  0.95555555555555
print()

   