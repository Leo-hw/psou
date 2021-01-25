#  로지스틱 회귀 분류 모델 : iris dataset    -  다항형 분류            // 앞으로 쭈욱 쓰게 될 형태.

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

iris = datasets.load_iris()
#print(iris.DESCR)
print(iris.data)
print(iris.target)
x = iris.data[:, [2, 3]]            # petal 만 참여
#x = iris.data
y = iris.target
print(x[:3])
print(y[:3])        # 0: setosa, 1:versicolor, 2:verginica

# train, test 로 자료 분리 ( 7 : 3 )
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state = 0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[:3])
'''
#스케일링 - 데이터 단위, 크기를 일정하게 분포. 정규화, 표준화
from sklearn.preprocessing import StandardScaler            # 표준화
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])        # iris 의 경우 데이터의 크기가 모두 일정하므로 스케일링 할 필요 없음.
'''

# 분류 모델 사용
#ml = LogisticRegression(C=1.0, random_state = 0) # C 속성 - L2 정규화에 의한 페널티 적용 -오버피팅(과적합) 방지

# SVC 분류 모델 사용
# from sklearn import svm
# ml = svm.SVC(C=1.0) 

# Gaussian naive bayes 모델 사용
# from sklearn.naive_bayes import GaussianNB
# ml = GaussianNB()

# RandomForestClassifier
#from sklearn.ensemble import RandomForestClassifier
#ml = RandomForestClassifier(n_estimators=500, criterion = 'entropy', random_state=1) 

#KNeighborsClassifier
# from sklearn.neighbors import KNeighborsClassifier
# ml = KNeighborsClassifier(n_neighbors = 3, weights = "distance")

# Perceptron
# from sklearn.linear_model import Perceptron
# ml = Perceptron(max_iter =1000, random_state=3)

# MLP
from sklearn.neural_network import MLPClassifier
ml = MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=100,  learning_rate_init=0.01, solver='adam')  # loss = 잔차

print(ml)
result = ml.fit(x_train, y_train)       # 학습 진행
print(ml)

#모델을 학습시킨 후, 모델 객체를 저장 후 불러다 사용 ---------------------------
import pickle
fileName = 'ex4model.sav'
pickle.dump(ml, open(fileName, 'wb'))
#읽기
ml = pickle.load(open(fileName, 'rb'))
#----------------------------------------------------------------------
# 분류 예측을 통한 모델 정확도 평가.
y_pred = ml.predict(x_test)
print('예측 값 : ', y_pred)
print('실제 값 : ', y_test)

print('총 갯수 : %d, 오류수 : %d'%(len(y_test), (y_test !=y_pred).sum()))
print('정확도  : %.3f'%accuracy_score(y_test, y_pred))

conf_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['실제값'])
print(conf_mat)
print('정확도2 : ',(conf_mat[0][0] + conf_mat[1][1] + conf_mat[2][2])/len(y_test))
print('정확도3 : ', ml.score(x_test, y_test))

# 사용자가 알고 싶은 새로운 값으로 예측
#new_data = np.array([[1.1, 1.1, 1.1, 1.1], [6.1, 5.1, 4.1, 3.1]])
new_data = np.array([[1.1, 1.1], [6.1, 5.1]])
new_pred = ml.predict(new_data)
print('새 값에 대한 예측 결과  : ', new_pred)        # [0 2]



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family='malgun gothic')      #그래프에서 한글깨짐 방지용
plt.rcParams['axes.unicode_minus']= False

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])
    
    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    
    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 안자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape) #Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.
    
    # X를 xx, yy가 축인 그래프상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())  
    
    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)
        
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')
    
    plt.xlabel('표준화된 꽃잎 길이')
    plt.ylabel('표준화된 꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=ml, 
                    test_idx=range(105, 150), title='scikit-learn제공')     
