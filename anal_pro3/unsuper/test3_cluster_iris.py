# iris dataset 으로 계층적 군집 분석 

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris_df.head(3))
print(iris_df.loc[0:2, ['sepal length (cm)','sepal width (cm)']])

distMatrix = pdist(iris_df.loc[0:4, ['sepal length (cm)','sepal width (cm)']], metric='euclidean')
#distMatrix = pdist(iris_df.loc[:, ['sepal length (cm)','sepal width (cm)']], metric='euclidean')
print('distMatrix ; ',distMatrix)

row_dist = pd.DataFrame(squareform(distMatrix))
print('row_dist \n', row_dist)

print()
from scipy.cluster.hierarchy import linkage, dendrogram
row_cluster = linkage(distMatrix, method='complete')
print('row_cluster: ', row_cluster)

df = pd.DataFrame(row_cluster, columns=['id1', 'id2', '거리', '멤버수'])
print('df : \n', df)

row_dendro = dendrogram(row_cluster)
plt.tight_layout()
plt.ylabel('distance')
plt.show()

from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage = 'complete')
x = iris_df.loc[0:4, ['sepal length (cm)','sepal width (cm)']]
labels = ac.fit_predict(x)
print('클러스터 분류 결과: ', labels)

plt.hist(labels)
plt.grid(True)
plt.show()