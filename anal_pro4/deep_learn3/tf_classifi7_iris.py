# iris dataset 으로 분류, ROC Curve 출력.

import  numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics._classification import accuracy_score,\
    classification_report

iris = load_iris()
print(iris.DESCR)
x = iris.data
print(x[:2])
y = iris.target
print(y)
names = iris.target_names
feature_names = names
print(feature_names)

# label 원 핫 인코딩
onehot = OneHotEncoder(categories = 'auto')
print(onehot)
y = onehot.fit_transform(y[:,np.newaxis]).toarray()
print(y[:5], y.shape)

# feature 표준화
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
print(x_scale[:2])

# train / test
x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.3, random_state = 1)

n_features = x_train.shape[1]
n_classes = y_train.shape[1]
print(n_features, '  ', n_classes)  #4    3
# ----------------------------------------------------

# n의 갯수 만큼 모델 생성을 위한 함수
def create_custom_model(input_dim, output_dim, out_nodes, n, model_name='model'):
    def create_model():
        model = Sequential(name = model_name)
        for _ in range(n):
            model.add(Dense(out_nodes, input_dim = input_dim, activation='relu'))       # hidden layer
            
        model.add(Dense(output_dim, activation='softmax'))        # output
        model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['acc'])
        return model
    return create_model
    
models = [create_custom_model(n_features, n_classes, 10, n, 'model_{}'.format(n)) for n in range(1,4)]

for create_model in models:
    print('@@@@@ START @@@@@')
    create_model().summary()
    
print('\n생성된 임의의 모델들을 학습한 후 평가 결과를 비교----')
history_dict = {}       # dict type
for create_model in models:
    model = create_model()
    print('model name : ', model.name)
    histories = model.fit(x_train, y_train, batch_size = 10, epochs=50, verbose=0, validation_split=0.3)
    score = model.evaluate(x_test, y_test, verbose = 0)
    print('test dataset loss : ', score[0])
    print('test dataset accuracy : ', score[1])
    history_dict[model.name] = [histories, model]
    
print(history_dict)


# 시각화 
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,6))
#print(fig, ax1, ax2)
for model_name in history_dict:
    #print('h_d : ', history_dict[model_name][0].history['acc'])
    val_acc =  history_dict[model_name][0].history['val_acc']
    val_loss =  history_dict[model_name][0].history['val_loss']
    ax1.plot(val_acc, label=model_name)
    ax2.plot(val_loss, label=model_name)
    ax1.set_ylabel('validation acc')
    ax2.set_ylabel('validation loss')
    ax2.set_xlabel('epochs')
    ax1.legend()
    ax2.legend()
plt.show()

print('\nROC curve - 분류 모델 성능 평가 기법 중 하나')
#  AUC값은 1에 가까워 질 수록 우수한 모델
plt.figure()
plt.plot([0,1],[0,1],'k--')

for model_name in history_dict:
    model = history_dict[model_name][1]
    y_pred = model.predict(x_test)
    fpr, tpr, _ = roc_curve(y_test.ravel(), y_pred.ravel())
    print('fpr : ',fpr)
    print('tpr : ', tpr)
    plt.plot(fpr, tpr, label = '{}, AUC value : {:.3f}'.format(model_name, auc(fpr, tpr)))
    
plt.xlabel('False Positive rate')
plt.xlabel('TRUE Positive rate')
plt.title('ROC Curve')
plt.legend() 
plt.show()

print('k겹 교차 검증을 통한 성능 측정---------------------')
#create_custom_model(input_dim, output_dim, out_nodes, n, model_name='model'):
create_model = create_custom_model(n_features, n_classes, 10, 3)
estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=2)
scores = cross_val_score(estimator, x_scale, y, cv = 10)
print('ACCURACY : {:0.2f}(+/-{:0.2f})'.format(scores.mean(), scores.std()))

print('위의 방법을 참고한 결과 4개의 레이어를 사용했을 떄(모델3) 뷴류 결과 가장 우수함으로 이를 채택 ----')
model = Sequential()
model.add(Dense(10, input_dim=4, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics = ['acc'])
print(model.summary())

model.fit(x_train, y_train, epochs=50, batch_size=10)
print('모델검증 : ', model.evaluate(x_test, y_test))

print()
y_pred = np.argmax(model.predict(x_test), axis = 1)
print('예측값: ', y_pred)
real_y = np.argmax(y_test, axis =1).reshape(-1,1)
print('실제값: ', real_y.ravel())
print('분류 실패 수 :',(y_pred.ravel() != real_y).sum( ))
print()

from sklearn.metrics import confusion_matrix, classification_report
print('confusion_matrix : \n', confusion_matrix(real_y, y_pred))
print('accuracy : ', accuracy_score(real_y, y_pred))
print('classification_report :\n ', classification_report(real_y, y_pred))

print('\n새로운 값으로 분류 예측 ----------------------------------')
new_x = [[5.1,3.5,1.4,0.2], [4.6,3.0, 1.4,2.2],[1.6,3.8,5.4,8.2]]
new_x = StandardScaler().fit_transform(new_x)
new_pred = model.predict(new_x)
print('new_pred : ', new_pred)
print('new_pred : ', np.argmax(new_pred, axis=1).flatten())