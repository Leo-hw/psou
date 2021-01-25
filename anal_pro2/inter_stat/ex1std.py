# 분산/표준편차 (데이터의 치우침을 표현하는 대표값)의 중요성
# 평균은 동일하나 분산/표준 편차 값이 다름으로 인해 전체적인 데이터의 모습이 달라질 수 있다.
# 통계는 분산의 마법이다.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


np.random.seed(1)
print(stats.norm(loc = 1, scale = 2).rvs(10))

centers = [1, 1.5, 2]
col = 'rgb'

std = 0.1
data_1 = []
for i in range(3):
    data_1.append(stats.norm(loc= centers[i], scale=std).rvs(100))
    #print(data_1)
    plt.plot(np.arange(len(data_1[i]))+ i *len(data_1[0]), data_1[i], '*', color=col[i])
plt.show()

print(np.mean(data_1))


std2 = 2            # 편차가 큼
data_2 = []
for i in range(3):
    data_2.append(stats.norm(loc= centers[i], scale=std2).rvs(100))
    #print(data_1)
    plt.plot(np.arange(len(data_2[i]))+ i *len(data_2[0]), data_2[i], '*', color=col[i])
plt.show()
print(np.mean(data_2))

print()