# https://datalab.naver.com/keyword/realtimeList.naver


from bs4 import BeautifulSoup
import urllib.request
import requests


url = 'https://datalab.naver.com/keyword/realtimeList.naver'
data = requests.get(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}).text
soup = BeautifulSoup(data, 'lxml')
# print(soup)
list =  soup.findAll('span', {'class':'item_title'})

count = 1
for i in list:
    print(str(count) + '위 ' + i.string)
    count += 1



