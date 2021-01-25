'''
영화 정보 읽기

'''

from bs4 import BeautifulSoup
import urllib.request
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data, 'lxml')

#print(soup)
#print(soup.select('div.tit3'))
for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())

print()
#방법 2
import requests
data = requests.get(url)
print(data.status_code, '  ', data.encoding)        # 몇 가지 정보를 얻을 수 있다.
datas = data.text
#print(datas)

datas = requests.get(url).text
soup = BeautifulSoup(datas, 'lxml')
#print(soup)
#m_list = soup.findAll('div', 'tit3')            # tag 명, 속성
m_list = soup.findAll('div', {'class':'tit3'})            # tag 명, 속성
#print(m_list)

#  순위표시
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count) + '위:' + title.string)
    count +=1