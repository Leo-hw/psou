# BeautifulSoup 으로 기상청 날씨 정보 읽기
 
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as req

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = req.urlopen(url)
rdata=data.read()
#print(rdata.decode('utf-8'))

soup = BeautifulSoup(req.urlopen(url), 'lxml')
#print(soup)

title = soup.find('title').string
wf = soup.find('wf')
print(title)
print(wf)
city = soup.find_all('city')
print(city)
cityDatas = []
for c in city:
    cityDatas.append(c.string)

  
df = pd.DataFrame()
df['city'] = cityDatas    
#print(df)

# df 에 최저 기온 칼럼 추가
tmefs = soup.select_one('location > data > tmef')           # 직계 자식
print(tmefs)

tmefs = soup.select_one('location  data  tmef')             #자손
print(tmefs)

tmefs = soup.select_one('location > province + city + data > tmef')
print(tmefs)

print(soup.select('data > tmn')[0])

tempMins = soup.select('location > province + city + data > tmn') # 형제노드1 + 형제노드2             형제노드2 + 형제노드1
tempDatas = []
for t in tempMins:
    tempDatas.append(t.string)

#컬럼 추가.
df['temp_min'] = tempDatas

# 컬럼명 변경
df.columns = ['지역', '최저기온']        
print(df.head(3), '  ', len(df))
