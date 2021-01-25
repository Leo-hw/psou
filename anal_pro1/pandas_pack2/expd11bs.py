# BeautifulSoup 모듈을 이용해 XML, HTML 문서를 읽어 처리

html_data = '''
<html><body>
<h1> 제목 태그</h1>
<p> 웹 페이지를 분석</p>
<p> 원하는 자료 추출</p>
</body></html>
'''
print(type(html_data))  #<class 'str'>

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')
print(type(soup))           #    <class 'bs4.BeautifulSoup'>
h1 = soup.html.body.h1

# 같은 element 가 있는 경우
p1 = soup.html.body.p
# DOM 을 이용 (next_sibling)
p2 = p1.next_sibling.next_sibling


print('h1 : ', h1.string)
print('p1: ', p1.string)
print('p2: ', p2.string)


print('\n find() 찾기')
html_data2 = '''
<html><body>
<h1 id='title'> 제목 태그</h1>
<p> 웹 페이지를 분석</p>
<p id='my'> 원하는 자료 추출</p>
</body></html>
'''

soup2 = BeautifulSoup(html_data2, 'lxml' )
print(soup2.p)
print(soup2.p.string)
print(soup2.find('p').string)
print(soup2.find('p', id='my').string)
print("#title:"+ soup2.find(id='title').string)
print("#my:"+ soup2.find(id='my').string)

print('\nfind_all() 메소드로 여러개의 대상 찾기')
html_data3 = '''
<html><body>
<h1 id='title'> 제목 태그</h1>
<p> 웹 페이지를 분석</p>
<p id='my'> 원하는 자료 추출</p>
    <div>
        <a href="https://www.naver.com">naver</a>
        <a href="https://www.daum.com">daum</a>
    </div>
</body></html>
'''
soup3 = BeautifulSoup(html_data3, 'lxml')

#print(soup3)

#예쁘게 보기
# print(soup3.prettify())

print(soup3.find('a'))
print(soup3.find('a').string)
print(soup3.find(['a']))
print(soup3.find_all(['a']))
print(soup3.findAll(['a']))
print(soup3.findAll('a'))

print()
links = soup3.findAll('a')
print(links)
for i in links:
    href = i.attrs['href']
    text = i.string
    print(href, '  ', text)

print(soup3.find_all('p'))    
print(soup3.find_all(['p','h1']))

print()
print('정규 표현식')
import re
links2 = soup3.find_all(href=re.compile(r'^https://'))
print(links2)
for i in links2 :
    print(i.attrs['href'])
    
# 메소드가 어떤 타입을 원하는 지, 반환하는 지를 잘 봐야함.
print('***'*10)
print('CSS selector 사용')

html_data4 = '''
<html><body>
<h1 id='title'> 제목 태그</h1>
<p> 웹 페이지를 분석</p>
<p id='my'> 원하는 자료 추출</p>
    <div id = "hello">
        <a href="https://www.naver.com">naver</a>
        <ul class = "world">
                <li>안녕</li>
                <li>반갑다</li>
        </ul>
    </div>
</body></html>
'''
soup4 = BeautifulSoup(html_data4, 'lxml')
aa = soup4.select_one("div#hello > a").string                  # 직계 div#hello > a   // 그냥 자식 div#hello  a
print('aa : ' , aa)
ul = soup4.select("div#hello > ul.world > li")
for i in ul:
    print("li : " + i.string)
    