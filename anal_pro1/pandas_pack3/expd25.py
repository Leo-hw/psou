# 네이버 메뉴중 영화 관람명 자료를 읽어 특정 연화를 간의 유사도 출력 
from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def movie_scrap(url):
    result = []
    for p in range(10):  # 1페이지만 참여
        r = requests.get(url + "&page=" +str(p))
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        #print(soup)
        title = soup.find_all("td",{"class":"title"})
        #print(title)
        sub_result = []
        for i in range(len(title)):
            sub_result.append(title[i].text.replace('\n','').replace('\r','').replace('\t','').replace('\별점','').replace('-','').replace('.','').replace('애비규환','')
                              .replace('S.W.A.T 특수기동대','').replace('스트리트 오브 파이어','').replace('신고','').replace('영화',''))
        result = result + sub_result
    return("".join(result))

aebi = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=198430&target=after")
dogul = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=193194&target=after")
swat = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37354&target=after")
street = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=10236&target=after")
before = movie_scrap("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=17773&target=after")
movies =[aebi, dogul, swat, street, before]
print(movies)

#참고로 가장 만히 언급된 단어 
words_basket = []
okt = Okt()
for mov in movies:
    words = okt.pos(mov)  # 형태소 분석 - 품사 태깅
    for w in words:
        if w[1] in ['Noun', 'Adjective'] and len(w[0]) >=2 :
            words_basket.append(w[0])
             
print(Counter(words_basket).most_common(50))


import time
time.sleep(2)
movies = [m.replace("영화","") for m in movies]

print('--------------')
def word_separate(movies):
    result = []
    for mov in movies:
        words = okt.pos(mov)  # 형태소 분석 - 품사 태깅
        one_result=[]
        for w in words:
            if w[1] in ['Noun', 'Adjective'] and len(w[0]) >=2 :
                one_result.append(w[0])
        result.append(" ".join(one_result))
    return result

word_list = word_separate(movies)
print(word_list)

#feature vector 와 작업: BOW
# 방법1
count = CountVectorizer(min_df=2)
count_dtm = count.fit_transform(word_list).toarray()
print(count_dtm)
cou_dtm_df = pd.DataFrame(count_dtm, columns = count.get_feature_names(), index = ['aebi', 'dogul', 'swat', 'street', 'before'])
print(cou_dtm_df)

print('~~~~TfidVectorizer: 단어의 빈도수 뿐만 아니라 단어의 종요성을 고려~~~~~')

#방법 2
idf_maker = TfidfVectorizer(min_df=2)
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
print(tfidf_dtm)
tfidf_dtm_df = pd.DataFrame(tfidf_dtm, columns = count.get_feature_names(),index = ['aebi', 'dogul', 'swat', 'street', 'before'])
print(tfidf_dtm_df)

print()
#코사인 유사도를 이용해 영화 간 유사도를 확인
def cosin_func(doc1, doc2):
    bunja = sum(doc1 * doc2)
    bunmo = ((sum(doc1 ** 2) * sum(doc1 ** 2)** 0.5))
    return bunja/bunmo

res = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        res[i,j] = cosin_func(tfidf_dtm_df.iloc[i],tfidf_dtm_df.iloc[j].values)
        
df = pd.DataFrame(res, \
                  index = ['aebi', 'dogul', 'swat', 'street', 'before'], 
                  columns = ['aebi', 'dogul', 'swat', 'street', 'before'] )
print(df)