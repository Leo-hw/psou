# 웹에서 특정 단어 검색 후 '명사'들 만 추출해 빈도 수를 구한 후, 워드 클라우드 출력

# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from boto.dynamodb import item
import webbrowser

#keyword = input('검색어 :' )
keyword = "감기"
#print(quote(keyword))

target_url = "https://www.donga.com/news/search?query=" +quote(keyword)
#print(target_url)

source_code = urllib.request.urlopen(target_url)
soup = BeautifulSoup(source_code, 'lxml')
#print(soup)

msg = ""
for title in soup.findAll('p', 'tit'):
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href']         
    #print(article_url)              # https://www.donga.com/news/article/all/20201113/103949199/1
    
    source_article = urllib.request.urlopen(article_url)            #  각각의 a 태그의 본문 스크랩핑
    soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
    # #content > div > div.article_txt
    contents = soup.select(' div.article_txt')
    for imsi in contents:
        item = str(imsi.find_all(text=True))
        #print(item)
        msg = msg +item

print(msg)

from konlpy.tag import Okt
from collections import Counter
nlp = Okt()

nouns = nlp.nouns(msg)
result = []     # 두 글자 이상의 단어만 담기 위한 list 변수

for imsi in nouns:
    if len(imsi) >1 :
        result.append(imsi)
        
print(result)
count = Counter(result)
print(count)

tag = count.most_common(50)     # 상위 50 개의 명사만 참여.

import pytagcloud 
taglist = pytagcloud.make_tags(tag, 100)
print(taglist)

# tag_image 생성 후 저장
pytagcloud.create_tag_image(taglist, 'word.png', size=(1920,1080), fontname='korean', rectangular=False)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

webbrowser.open('word.png')
