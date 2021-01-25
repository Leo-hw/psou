'''
구글 검색 기능 이용 : 검색 결과의 갯수 만큼 브라우저의 탭을 열어, a tag 의 결과 출력

'''

import requests
from bs4 import BeautifulSoup
import webbrowser

def searchFunc():
    base_url = 'https://www.google.com/search?q={0}'
    sword = base_url.format('파이썬') 
    print(sword)
    plain_text = requests.get(sword, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
    print(plain_text)
    soup = BeautifulSoup(plain_text.text, 'lxml')
    
    #print(soup)
    link_data = soup.select('div > div.yuRUbf > a')
    #print(link_data)
    for link in link_data[:3]:
        print(link)
        print(type(link), ' ', type(str(link)))
        print(str(link).find('https'), ' ', str(link).find('onmousedown') - 2)
        # 데이터는 str(link)가 들고 있음. 뒤의 내용은 슬라이싱을 위함.
        urls = str(link)[str(link).find('https'):str(link).find('onmousedown') - 2]         # 슬라이싱 예 => [9:57]
        print(urls)
        
        webbrowser.open(urls)
        
searchFunc() 