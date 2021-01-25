# pandas 로 파일 저장
import pandas as pd

items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)

df.to_csv('expd7rep1.csv', sep=',')
df.to_csv('expd7rep2.csv', sep=',',index = False)
df.to_csv('expd7rep3.csv', sep=',', index = False, header = False)  # 색인 + header 제외

data = df.T
print(data)
data.to_csv('expd7rep4.csv', sep=',')
data.to_html('expd7rep5.txt')

print('\nExcel 관련 파일 처리')
df2  = pd.DataFrame({'data':[1,2,3,4,5]})
print(df2)

#저장(엑셀 파일로)
toexc = pd.ExcelWriter('expd7rep5.xlsx', engine='xlsxwriter')
df2.to_excel(toexc, sheet_name='Sheet1' )
toexc.save()

#읽기
exf = pd.ExcelFile('expd7rep5.xlsx')
print(exf.sheet_names)
df3 = exf.parse('Sheet1')
print(df3)

print()
df4 = pd.read_excel(open('expd7rep5.xlsx', 'rb'), sheet_name='Sheet1')      # read binary
print(df4)

train = pd.read_csv('https://raw.githubusercontent.com/Leo-hw/Lesson/master/train.csv')
print(train)
