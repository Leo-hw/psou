# BOW : 단어의 빈도수를 부여해 feature vector 를 만들어 빈도 수 저장.
# 한글 어간 추출 : '봄은' , '봄과' , '봄이' => '봄'으로 통일

import numpy as np
#from konlpy.tag import Okt
from konlpy.tag import Okt


str_data = np.array(['봄은' , '봄과' , '봄이'])
#print(str_data)
okt = Okt()
# 텍스트로 정제
my_words =[]
for i, doc in enumerate(str_data):
    for word in okt.pos(doc, stem=True):
        #print(word)
        if word[1] in ['Noun']:
            my_words.append(word[0])
            
print(my_words)

print('\n -----------------------------------------------------------------')
content = ['How to format my hard disk.','Hard Disk format format problems.']
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#CountVectorizer : 단어 토큰을 생성해 각 단어의 수를 세어 BOW 벡터를 생성, 띄어쓰기 기준
#TfidfVectorizer  : 단어의 가증치를 조정한 BOW 벡터를 생성, 띄어쓰기 기준

# 방법1) CountVectorizer
count_vec = CountVectorizer(analyzer='word', min_df=1)        #analyzer='char'
print(count_vec)

aa = count_vec.fit_transform(content)
print(aa)
print(count_vec.get_feature_names())
print(aa.toarray())


# 방법2 ) TfidfVectorizer
tfidf_vec = TfidfVectorizer(analyzer='word',min_df=1)
print(tfidf_vec)
bb = tfidf_vec.fit_transform(content)
print(bb)
print(tfidf_vec.get_feature_names())
print(bb.toarray())


print('\n\n한글 데이터로 CountVectorizer ---------------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지','내일 공부 해야겠다.','점심 먹고 공부 해야지']
#count_vec = CountVectorizer()
count_vec = CountVectorizer(analyzer='word', min_df=1, ngram_range=(1,1))       # default
#count_vec = CountVectorizer(analyzer='word', ngram_range=(3,3))       # default
#count_vec = CountVectorizer(analyzer='word', min_df=1, max_df=5)       # 빈도수 ㅣ 최소 1회, 최대 5회
#count_vec = CountVectorizer(analyzer='word', stop_words=['나는', '해야지'])          #불용어 등록.(추가만 함) 제거를 위해서 따로 ㅁ[ㅔ소드 만들어야함.    

count_vec.fit(text_data)
print(count_vec.get_feature_names())
print(count_vec.vocabulary_)
# default {'나는': 2, '고프다': 0, '아니': 7, '배가': 6, '내일': 3, '점심': 8, '먹지': 5, '공부': 1, '해야겠다': 9, '먹고': 4, '해야지': 10}
# ngram_range = 3,3 {'나는 고프다 아니': 1, '고프다 아니 배가': 0, '아니 배가 고프다': 5, '내일 점심 먹지': 3, '내일 공부 해야겠다': 2, '점심 먹고 공부': 6, '먹고 공부 해야지': 4}
# max_df =5 {'나는': 2, '고프다': 0, '아니': 7, '배가': 6, '내일': 3, '점심': 8, '먹지': 5, '공부': 1, '해야겠다': 9, '먹고': 4, '해야지': 10}
print(text_data[0])
sentence = [text_data[0]]
print(count_vec.transform(sentence))
print(count_vec.transform(sentence).toarray())

new_sentence = ['나는 공부 이건 점심 먹고 공부 해야 배가 부르다 라고 느낀다']
print(count_vec.transform(new_sentence).toarray())
print(count_vec.transform(new_sentence).toarray().sum(axis=1))

# 횟수를 사용해 벡터를 만듦으로 해서, 직관적으로 파악
# 중복이 많은 경우 문제 잇음, 위의 경우 의미가 없는 단어가 작업에 참여하므로 어간 추출이 필요.

my_words =[]
for i, doc in enumerate(text_data):
    for word in okt.pos(doc, stem=True):
        #print(word)
        if word[1] in ['Noun','Adjective', 'Verb']:
            my_words.append(word[0])
            
print(my_words)
count_vec.fit(my_words)
print(count_vec.transform(my_words).toarray())

print('\n\n한글 데이터로 TfidfVectorizer ---------------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지','내일 공부 해야겠다.','점심 먹고 공부 해야지']

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text_data)
print(tfidf_vectorizer.get_feature_names())
print(tfidf_vectorizer.vocabulary_)
print()
print(tfidf_vectorizer.transform(text_data).toarray())

sentence = [text_data[3]]
print(tfidf_vectorizer.transform(sentence))
print(tfidf_vectorizer.transform(sentence).toarray())

# 1(공부), 8(점심) 번째 0.43779123108611473 의 값을 가짐.
# 빈도 수에 있어서 1,8 번째가 조금 더 관련이 있다. 
# 4(먹고), 10(해야지) 번 째 단어가     0.5552826649411127 정도의 값을 가짐.
