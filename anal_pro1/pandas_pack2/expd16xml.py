'''
beautifulsoup 으로 xml 데이터 
'''
from bs4 import BeautifulSoup

with open("my.xml", mode = 'r', encoding='utf8') as f:
    xmlfile = f.read()
    print(xmlfile, type(str))
    
soup = BeautifulSoup(xmlfile, 'html.parser')
print(type(soup))
#print(soup.prettify())
itemTag = soup.findAll('item')
print(itemTag[0])

print()
nameTag = soup.findAll('name')
print(nameTag[0]['id'])
for i in nameTag:
    print(i['id'])
    
for i in itemTag:
    nameTag = soup.findAll('name')
    for j in nameTag:
        print('id:' + j['id']+ '  name :' + j.string)
        tel = i.find('tel')
        print('tel : ' + tel.string)
    print()
    for j in i.find_all('exam'):
        print('kor :'+ j['kor']+' eng : '+ j['eng'])


print('----------------------------------------------------------------------')
# 웹에서 XMl 문서 읽기 = 도서관 정보
import urllib.request as req

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoullibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
print(plainText)

xmlObj = BeautifulSoup(plainText, 'lxml')
libData = xmlObj.select('row')
#print(libData)

for d in libData:
    name = d.find('lbrry_name').text
    addr = d.find('adres').text
    print('도서관 명 :' + name + ' 주소 : ' + addr)