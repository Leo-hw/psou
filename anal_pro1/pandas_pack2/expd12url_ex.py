'''
BBQ 사이트에서 메뉴정보 읽어오기..
'''
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://www.bbq.co.kr/menu/menuList.asp"
bbq = req.urlopen(url)
#print(url)
#document.querySelector("body > div.wrapper.scrolled > div.container > article > section > div.section-body > div > div:nth-child(50) > div.info > p.name")
#document.querySelector("body > div.wrapper.scrolled > div.container > article > section > div.section-body > div > div:nth-child(50) > div.info > p.pay")

soup = BeautifulSoup(bbq, 'html.parser')
#print(soup)
mdata = soup.select("div.info > p.name")
#print(mdata)
pdata = soup.select("div.info > p.pay")
#print(pdata)

datas=[]
import re

for d,p in zip(mdata, pdata): 
    pmenu = d.string
    menu = re.sub(r'[\d+,→(랜덤)]','', pmenu)
    price = p.string
    #가격 자료에서 , 없애기
    price_re = price.replace(',','').replace('원','')
    datas += [[menu, int(price_re)]]
#print(datas) 

from pandas import DataFrame
df = DataFrame(datas, columns=['name','pay'])

print(df)
print("-----")
print('가격평균:', round(df['pay'].mean(), 1))
print('최대가격:', df['pay'].max())
print('최소가격:', df['pay'].min())
print('표준편차:', round(df['pay'].std(), 1))
print('상품 건수 :', len(df))
