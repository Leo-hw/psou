
import pandas as pd
import matplotlib.pyplot 


train = pd.read_csv('./input/train.csv')
test = pd.read_csv('C:/work/psou/pro1/pack3/input/test.csv')



# 위에서 5개의 데이터를 칼럼명과 함께 표시 (비어있을 경우, 기본값: 5)

test.head(5)
# 위에서 10개의 데이터 칼럼명과 함께 표시
train.head(10)
train.info()
print('--------------------------------------')
test.info()
train.isnull().sum()

# 행의 개수, 열의 개수 반환
# (891, 12)
train.shape
