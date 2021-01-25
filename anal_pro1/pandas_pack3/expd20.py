# 웹문서를 읽어 형태소 분석

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse        # 한글 인코딩용 모듈

okt = Okt()

#para = '이순신'
#한글은 인코딩이 필요
para =  parse.quote('이순신')
url = 'https://ko.wikipedia.org/wiki/' + para
#print(url)          

page = urllib.request.urlopen(url)
#print(page)

soup = BeautifulSoup(page.read(), 'lxml')
#print(soup)             # #mw-content-text > div.mw-parser-output > p:nth-child(6)

wordlist = []
for item in soup.select("#mw-content-text > div > p"):
    #print(item)
    if item.string != None:
        #print(item.string)
        ss = item.string
        #print(okt.nouns(ss))
        wordlist += okt.nouns(ss)
        
        
print('wordlist : \n', wordlist)
print('단어 수 : ' + str(len(wordlist)))
print()

word_dict = {}                  # 단어의 횟수를 dict type 으로 기억.
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print('word_ dict : ' , word_dict)

setData = set(wordlist) # 중복 제거
print('중복이 없는 단어 수 : ' + str(len(setData)))
 

print('\n Series type 시리즈 타입으로 처리')
import pandas as pd

wolist = pd.Series(wordlist)
print(wolist[:3])
print(wolist.value_counts()[:5])

print()
woDict = pd.Series(word_dict)
print(woDict[:3])
print(woDict.value_counts()[:5])

print('\n DataFrame 으로 출력(판다스)')
df1 = pd.DataFrame(wordlist, columns = ['단어'])
print(df1.head(3))
print()

df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
print(df2)
df2 = df2.T
df2.columns = ['단어','빈도수']
print(df2)

df2.to_csv('이순신.csv' , sep = ',', header=True, index=False)
df3 = pd.read_csv('이순신.csv')
print(df3.head(5))