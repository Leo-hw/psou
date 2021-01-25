# [분류분석 문제1]
# 문1] 소득 수준에 따른 외식성향을 나타내고 있다.
# 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection._split import train_test_split
import matplotlib.pyplot as plt

fdata = pd.read_csv('C:/work/psou/anal_pro3/classification/ex2_model.txt')
data = fdata.loc[(fdata['요일']=='토') | (fdata['요일']=='일')]
print(data) 

 
 
 
