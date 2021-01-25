'''
Created on 2020. 11. 13.

@author: KITCOOP
'''
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse        # 한글 인코딩용 모듈
import pandas as pd

# http://www.seelotus.com/gojeon/gojeon/so-seol/hong-kil-dong-wan-pan-bon.htm

okt = Okt()

url = 'http://www.seelotus.com/gojeon/gojeon/so-seol/hong-kil-dong-wan-pan-bon.htm'

page = urllib.request.urlopen(url)
print(page)

soup = BeautifulSoup(page.read(), 'lxml')

wordlist = []
count = []
#print(soup.select('body  table  tr  td  p'))
data = soup.select('body > table > tr > td > p')
# for 문으로 dataframe 에 입력
for item in data:
    if item.string != None:
        ss = item.string
        #print(ss)
        for w in okt.nouns(ss) : 
            if len(w) > 1 :
                
                word = okt.pos
                wordlist.append(w)

#print('wordlist : ' , wordlist)
df = pd.DataFrame(wordlist)
df.columns = ['단어']
#print(df)


df2= df.sort_values(by='단어',ascending=True).head(10)
print(df2)
#저장(엑셀 파일로)
toexc = pd.ExcelWriter('홍길동.xlsx', engine='xlsxwriter')
df.to_excel(toexc, sheet_name='Sheet1' )
toexc.save()
