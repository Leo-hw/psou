# 멀티 프로세싱을 이용한 웹 스크래핑// 시간을 중요하게 볼 것

import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_links(): # 특정 사이트의  하이퍼링크를 가져오기
    data = requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup = bs(data, 'html.parser')
    #print(soup)
    my_titles = soup.select('h3>a')
    data = []
    for title in my_titles:
        data.append(title.get('href'))
    return data
    
def get_content(link):
    abc_link = 'https://beomi.github.io'+link
    data = requests.get(abc_link).text
    soup = bs(data, 'html.parser')
    #가져온 데이터로 뭔가를 ... 그러나 우리는 그저 소요시간을 궁금할 따름...
    print(soup.select('h1')[0].text)#첫번째 h1 tag 텍스트 하나만 찍어봄
    
    
if __name__ == '__main__':
    start_time = time.time()
    '''
    #print(get_links())
    for link in get_links():
        get_content(link)
    '''
    pool = Pool(processes = 5)    # 5개의 process 사용
    pool.map(get_content, get_links())      # 함수 와 인자값을 매핑하면서 처리(함수, argument)
    print('----%s 초 ----'%(time.time()-start_time))
    
