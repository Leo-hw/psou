# 뉴스 문서를 읽어 형태소 분석 후 파일로 저장, 단어별 유사도 출력
import pandas as pd
from konlpy.tag import Okt

okt  = Okt()

with open('daumnews.txt', mode='r', encoding='utf-8') as f:
    #print(f.read())
    lines = f.read().split('\n')
    print(len(lines))
    
wordDic = {}

for line in lines:
    datas = okt.pos(line)       # 품사 태깅
    #print(datas)        
    
    for word in datas:
        if word[1] == 'Noun':           # 명사만 작업
            print(word[0])
            print(word[0] in wordDic)
            
            if not(word[0] in wordDic):
                wordDic[word[0]] = 0
            wordDic[word[0]] += 1
            
print(wordDic)      # {'오늘': 1, '노': 1, '마스크': 32, ....

# 건수 별 내림차순 정렬
keys = sorted(wordDic.items(), key= lambda x:x[1], reverse = True)
print(keys)


#DataFrame 에 단어와 건수 담기.
wordList = []
countList = []

for word, count in keys[:20]: # 건수 상위 20개만 작업
    wordList.append(word)
    countList.append(count)
    
df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df)

print(' ---------------------------------------------------------------------------------------------------------------------------------- ')
results = []
with open('daumnews.txt', mode='r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    
    for line in lines:
        datas= okt.pos(line, stem = True)
        print(datas)
        imsi = []
        for word in datas:
            if not word[1] in ['Josa', 'Suffix','Punctuation','Determiner', 'Alpha', 'Number', 'Verb']:
                imsi.append(word[0])
                
                imsi2 = ("" . join(imsi)).strip()
        results.append(imsi2)
print(results)

fileName = 'daumnews2.txt'
with open(fileName, mode='w', encoding='utf-8') as fw:
    fw.write('\n' .join(results))
    print('저장성공')

print('\ 워드 임베딩(단어를 수치화해서 벡터로 기억 - 단어/문장 간 관련성(유사도) 계산, 전이학습..')

# One - hot encoding : 단어를 인덱싱하여 최소 벡터화
# Word2vec : 문맥이 유사한 단어를 비슷한 벡터로 표현
# pip install gensim

from gensim.models import word2vec
import numpy as np

# 간단한 예
#sentence = [['python', 'lan', 'program', 'computer', 'say']]
one_sentence = ['python', 'lan', 'program', 'computer', 'say']
print(one_sentence)

# One-hot encoding 처리
values = []
for x in range(len(one_sentence)):
    values.append(x)
print(values)
values_len = len(values)

one_encoding = np.eye(values_len)[values]
print(one_encoding)
#문자열이 있는 곳만 1로 표시하고 나머지는 0으로 표기 하는 것을 one-hot encoding

# Word2vec 처리
sentence = [['python', 'lan', 'program', 'computer', 'say']]

model = word2vec.Word2Vec(sentence, min_count=1, size=50)
word_vectors = model.wv
print('model.wv.vocab :', word_vectors.vocab)       # vocab 객체(object)가 만들어짐// 실제로 할 때는 필요 없는 과정, 지금은 과정을 보기 위함.

vocabs = word_vectors.vocab.keys()
print('vocabs :', vocabs)
vocab_val = word_vectors.vocab.values()
print('vocab_val', vocab_val)
word_vectors_list = [word_vectors[v] for v in vocabs]
print(word_vectors_list)
print(word_vectors_list[0], '  ', len(word_vectors_list[0]))
print(len(word_vectors_list))
print(word_vectors.similarity(w1='lan', w2='program'))

print(model.wv.most_similar('lan'))
print(model.wv.most_similar('python'))            

# daumnews2.txt 파일자료를 읽어 단어 간 유사도 파악
genObj = word2vec.LineSentence(fileName)
print(genObj)

# 분석 방법론
# wikidocs
# CBOW 주변단어로 중심단어를 예측 / 나는 ~ 간다.
# Skip-gram  : 중심단어로 주변단어를 예측 / ~ 외나무 다리 ~
model = word2vec.Word2Vec(genObj, size=100, window=10, min_count=2, sg =1) # sg=1, skip-Gram /sg =0 CBOW
print(model)

model.init_sims(replace=True)       # 필요없는 메모리 해제

# 학습된 모델을 저장 후 재 사용
try:
    model.save('news.model')
except Exception as e:
    print('err :' ,e)
    
# 모델 읽기
model = word2vec.Word2Vec.load('news.model')
print(model.wv.most_similar(positive=['마스크']))          # positive 단어사전에 단어가 있을 확률
print(model.wv.most_similar(positive=['마스크'], topn=3)) 
print(model.wv.most_similar(positive=['마스크', '흡연'], negative=['음료']))             

        