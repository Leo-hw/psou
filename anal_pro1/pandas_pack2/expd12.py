# BeautifulSoup 모듈로 wikipedia 자료 읽기

import urllib.request   as req
from bs4 import BeautifulSoup

url= 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
wiki = req.urlopen('https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0')
#print(wiki)

#soup = BeautifulSoup(wiki, 'html.parser')
soup = BeautifulSoup(wiki, 'html.parser')
#print(soup)
# #mw-content-text > div.mw-parser-output > p:nth-child(37) > a:nth-child(6)
# mw 클래스 직계 / div 직계 / p 직계/a
print(soup.select('#mw-content-text > div.mw-parser-output > p'))
print(soup.select(r'^[A-Za-z]#mw-content-text > div.mw-parser-output > p'))

print(' ^^^' * 10)
# daum 사이트의 뉴스 정보 읽기
url2 = 'https://news.v.daum.net/v/20201112100744370'
daum = req.urlopen(url2)
#print(daum)
import bs4 
soup2 = bs4.BeautifulSoup(daum, 'lxml')
# css selector
print(soup2.select_one('div#kakaoIndex > a').string)
datas = soup2.select('div#kakaoIndex a')
print(datas)
print()
for i in datas:
    #print(i)
    href = i.attrs['href']
    text = i.string
    print('href:%s, text:%s'%(href, text))
    print('href:{}, text:{}'.format(href, text))

print()
# find() 이동
#datas2 = soup2.findAll('a')
datas2 = soup2.find_all('a')
print(datas2)
for i in datas2[:2]:
    href = i.attrs['href']
    text = i.string
    print('href:%s, text:%s'%(href, text))
    
print()     # 본문 읽기   #harmonyContainer > section > p:nth-child(8)
datas3 = soup2.select('#harmonyContainer > section > p')
print(datas3)

for i in datas3[:3]:
    print(i.string)