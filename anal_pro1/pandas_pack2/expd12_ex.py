'''
bbq 홈페이지 에서 메뉴명과 가격을 읽어와서 dataframe 에 담고, 
 평균 가격, 가장 비싼 가격, 싼 가격, 표준편차
'''
import urllib.request as req
from bs4 import BeautifulSoup
from bokeh.util.sampledata import DataFrame

url = 'https://m.bbq.co.kr/menu/menuList.asp?anc=99999'
datas = req.urlopen('https://m.bbq.co.kr/menu/menuList.asp?anc=99999')
#print(datas)
soup = BeautifulSoup(datas, 'html.parser')
#print(soup)
# #body > div.wrapper.scrolled > div > article > div.menu_accordion.inbox1000.menu_accordion_fix > div
# #list_div_17

# body > div.wrapper.scrolled > div
bbq = soup.select('body > div.wrapper > div > article > div.menu_accordion.inbox1000 > div')
#bbq = soup.find_all(['strong'])
#print(bbq)
#print(soup.find_all(['a']))
price = soup.find_all(['strong'])
print(price)
menu = soup.find_all(['h4'])
print(menu)

import pandas as pd

#print(menu.describe())
item = []
for i in price:
    pr = i.get_text()
    pr = pr.replace(',', '')
    pr = pr.replace('원', '')
    pr.strip()
    pr = int(pr)
    #print(pr)
    item.append(pr)

list =[]
for j in menu:
    mn = j.get_text()
    #mn = mn.replace()
    #print(mn)
    mn.strip()
    list.append(mn)


#itemlist = pd.DataFrame(columns=['menu','price'])
#df = pd.DataFrame([ x for x in zip(lst_A,lst_B)])
itemlist = pd.DataFrame([x for x in zip(list, item)])
#df.rename(columns = {'old_nm' : 'new_nm'), inplace = True)
itemlist.rename(columns={0:'menu',1:'price'}, inplace = True)

print(itemlist.head())
print('가격 전체 합 : ',itemlist['price'].sum())
print('가격 전체 평균 : ',round(itemlist['price'].mean(),2)   )
print('가격 전체 표준 편차: ',round(itemlist['price'].std(),2))
print(itemlist['price'].max())
print(itemlist['price'].min())    
# itemlist.append(item)
# itemlist.append(list)
#print(itemlist.head())
    
    #menu.insert(loc=[1],column='price', value=i)
    #print(i.attrs['a'])
    