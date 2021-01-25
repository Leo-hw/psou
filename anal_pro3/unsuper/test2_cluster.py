# 계층적 군집분석 : 계층적으로 군집(cluster)을 나누는  분석 방법. 비지도학습
# 응집형 - 자료를 계속 가까운 것끼리 연결해가며 군집의 크기(수)를 늘려가는 방법. - 상향식
# 데이터의 양이 많으면 문제 발생

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

np.random.seed(1)
var = ['x', 'y']
labels = ['점0','점1','점2','점3','점4']
#labels = [1,0,2,0,1]
x = np.random.random_sample([5,2]) *10
df = pd.DataFrame(x, columns = var, index = labels)
print(df)

plt.scatter(x[:,0], x[:,1], s=50, c='blue', marker='o')
plt.grid(True)
plt.show()

from scipy.spatial.distance import pdist, squareform
distMatrix = pdist(df, metric='euclidean')  # n-차원 공간의 객체 간의 거리를 반환 
print('distMatrix : ', distMatrix)

row_dist = pd.DataFrame(squareform(distMatrix), columns = labels, index = labels)
print(row_dist)

# linkage() 를 이용해 응집형 클러스터링을 수행
from scipy.cluster.hierarchy import linkage
row_cluster = linkage(distMatrix, method = 'ward')
print(row_cluster)

df = pd.DataFrame(row_cluster, columns = ['군집1', '군집2', '거리', '군집멤버수'], index = ['군집%d'%(i+1) for i in range(row_cluster.shape[0])])

print(df)

from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels = labels)
plt.tight_layout()
plt.ylabel('유클리드거리')
plt.show()

print()
#계층적 클러스터링에 대해 최종적으로 분류된 정보 보기 
from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage = 'ward')
labels = ac.fit_predict(x)
print('클러스터 분류 결과: ', labels)

a = labels.reshape(-1, 1)
print(a)
x1 = np.hstack([x,a])
print(x1)
x_0 = x1[x1[:,2]==0, :]
x_1 = x1[x1[:,2]==1, :]
x_2 = x1[x1[:,2]==2, :]
plt.scatter(x_0[:, 0], x_0[:, 1])
plt.scatter(x_1[:, 0], x_1[:, 1])
plt.scatter(x_2[:, 0], x_2[:, 1])
plt.legend(['cluster0', 'cluster1', 'cluster2'])
plt.show()