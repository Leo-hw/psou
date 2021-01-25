# https://blog.itpaper.co.kr/python-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%A0%95%EC%A0%9C/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = 'Malgun Gothic'

# DataFrame화
txt = np.genfromtxt('linear_ex.txt', delimiter=',', encoding = 'utf8')[1:]
data = pd.DataFrame(txt)
data.columns = ['구분','지상파','종편','운동']

# 이상치 확인 시각화
data.boxplot()
plt.show() # 운동만 이상치 하나 있는 거 확인

# outlier 제거
outlier = data.query('운동 > 24')
print(outlier)

outlier_index = list(outlier.index)
print(outlier_index)

# outlier → NaN 처리
for i in outlier_index:
    data.loc[i, '운동'] = np.nan

print(data)