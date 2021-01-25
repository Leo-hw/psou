# 네이버 메뉴 중 영화 관람 평 자료를 읽어 특정 영화들 간의 유사도 출력

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer



def movie_scrap(url):
    result = []
    for p in range(10): # 10페이지만 참여
        r = requests.get(url + "&page="+str(p))
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        #print(soup)
        ##old_content > table > tbody > tr:nth-child(1) > td.title
        title = soup.find_all("td", {"class":"title"})
        #print(title)
        sub_result = []
        for i in range(len(title)):
            sub_result.append(title[i].text
                              .replace('\n', '')
                              .replace('\r','')
                              .replace('\t','')
                              .replace('별점','')
                              .replace('-','')
                              .replace('.','')
                              .replace('신고','')
                              .replace(',','')
                              .replace('애비규환','')
                              .replace('S.W.A.T특수공작대','')
                              .replace('도굴','')
                              .replace('스트리트 오브 파이어','')
                              .replace('죽은 시인의 사회',''))
        result = result + sub_result
    return("".join(result))

        
#https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=198430&target=after
aebi = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=198430&target=after')
dogul = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=193194&target=after')
dead = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=10048')
swat = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37354&target=after')
street = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=10236&target=after')

movies = [aebi, dogul, dead, swat, street]
print(movies)

# 참고로 가장 많이 언급된 단어
words_basket = []
okt = Okt()
for mov in movies:
    words = okt.pos(mov)     # 형태소 분석 - 품사 태깅
    for w in words:
        if w[1] in ['Noun', 'Adjective'] and len(w[0]) >= 2:
            words_basket.append(w[0])
 
print(Counter(words_basket).most_common(50))

import time
time.sleep(2)
movies = [m.replace("영화", "") for m in movies]      # 웹에서는 조금씩 텀을 주고 작업 하는 것이 좋음.

print('----------------------------------------------------------------------------------------------------------------------')

def word_separate(movies):
    result = []
    for mov in movies:
        words = okt.pos(mov)            
        one_result = []
        for w in words:
            if w[1] in ['Noun', 'Adjective'] and len(w[0]) >=2:
                one_result.append(w[0])
        result.append("".join(one_result))
    return result

word_list = word_separate(movies)
print(word_list)

# feature vector 화 작업 : BOW
print('~~~~~~~~~~~~~~~~~CountVectorizer~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
# 방법 1: 
count = CountVectorizer(max_df = 30)
count_dtm = count.fit_transform(word_list).toarray()
#print(count.get_feature_names())
print(count_dtm)

pd.set_option('display.max_columns', 500) # 생략 없이 전체 보기.

cou_dtm_df = pd.DataFrame(count_dtm, columns = count.get_feature_names(), index=['aebi', 'dogul', 'dead', 'swat', 'street'])

print(cou_dtm_df)

time.sleep(2)
print('~~~~~~~~~~~~~~~~~~~TfidfVectorizer : 단어의 빈도 수 뿐 만 아니라 단어의 중요성을 고려~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 방법 2
idf_maker = TfidfVectorizer(min_df = 1)
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
print(tfidf_dtm)
tfidf_dtm_df = pd.DataFrame(tfidf_dtm, columns = count.get_feature_names(),
                            index=['aebi', 'dogul', 'dead', 'swat', 'street'])
print(tfidf_dtm_df)

print()
# 코사인 유사도를 이용해 영화 간 유사도를 확인
def cosin_func(doc1, doc2):
    bunja = sum(doc1 * doc2)
    bunmo = (sum(doc1**2) * sum(doc2**2))**0.5
    return bunja / bunmo

res = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        res[i, j] = cosin_func(tfidf_dtm_df.iloc[i], tfidf_dtm_df.iloc[j].values)
        
df = pd.DataFrame(res, 
                  index=['aebi', 'dogul', 'dead', 'swat', 'street'],
                  
                  columns=['aebi', 'dogul', 'dead', 'swat', 'street'])
print(df)


    
