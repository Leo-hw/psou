'''
Created on 2020. 11. 11.

@author: KITCOOP
'''
import pandas as pd
#import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df.head())

print(df.iloc[:,1:3])
print(df['Survived']==1)
#df2 = df['Survived'!=1].drop('d')  
counts = df['Survived'].value_counts()
counts2 = df['Pclass'].value_counts()
print(counts)
print(counts2)
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]

df["age_cat"] = pd.cut(df["Age"], bins, labels=labels)
print(df['age_cat'].value_counts())
# pivot 테이블 사용시 자동으로 평균값 mean 을 구해줌(group by 와  mean)
dfp=round(pd.pivot_table(df, index=['Sex', 'age_cat'], columns='Pclass', values='Survived', fill_value=0)*100, 2)
print(dfp)

human = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
human_df = human.rename(columns=lambda x: x.strip())
#human_df['Group']=human_df['Group'].str.strip()
print(human_df.head())
print(human_df.columns)
print(human_df.dropna(subset=['Group']))
human_df2 = pd.DataFrame(human_df, columns=['Career', 'Score'])
print(human_df2.mean())

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv')
print(df.head(3))
print(df.info())
print(df.describe())
print(df['smoker'].value_counts())
print(df['day'].unique())