# data.co.kr에서 관광지 자료를 읽음
# 국내 관광지에 대해 미국인, 일본인, 중국인 관광객 출입 데이터로 상관관계 분석
import json
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import pandas as pd
import numpy as np

def setScatterChart(tour_table, all_table, tourpoint):
    # 계산할 관광지명에 해당하는 자료만 뽑아서 tour 변수에 저장하고, 외국인 관광객 자료와 병합
    tour = tour_table[tour_table['resNm']==tourpoint]
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    print(merge_table)
    
    # 시각화
    fig = plt.figure()
    fig.suptitle(tourpoint + '상관관계 분석')
    
    plt.subplot(1,3,1)
    plt.xlabel('중국인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    print('r1 : ', r1)
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], alpha=0.8, s=6, c='black')
    
    plt.subplot(1,3,2)
    plt.xlabel('일본인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    print('r2 : ', r2)
    plt.title('r={:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], alpha=0.8, s=6, c='red')
    
    plt.subplot(1,3,3)
    plt.xlabel('미국인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    print('r3 : ', r3)
    plt.title('r={:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], alpha=0.8, s=6, c='blue')
    
    plt.tight_layout()
    plt.show()
    return [tourpoint, r1, r2, r3]


def Gogo():
    # 서울시 관광지 정보 파일을 읽어 DataFrame 에 저장
    fname =  '서울특별시_관광지.json'
    jsonTp = json.loads(open(fname, 'r', encoding='utf-8').read())  # str -> dict type (decoding)
    #print(jsonTp)
    tour_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'resNm', 'ForNum'))
    tour_table = tour_table.set_index('yyyymm')
    #print(tour_table)
    
    resNm = tour_table.resNm.unique()
    #print(resNm)
    print('관광지명 : ', resNm[:5]) 
    
    # 중국인 관광지 정보파일 읽기
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='utf-8').read())
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    #print(china_table)
    
    # 일본인 관광지 정보파일 읽기
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    #print(japan_table)
    
    # 미국인 관광지 정보파일 읽기
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    #print(usa_table)
    
    all_table = pd.merge(china_table, japan_table, left_index= True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index= True, right_index=True)
    #print(all_table, ' ', all_table.shape)
    
    r_list = []
    for tourpoint in resNm[:5]:
        #print(tourpoint)
        r_list.append(setScatterChart(tour_table, all_table, tourpoint))
    
    r_df = pd.DataFrame(r_list, columns=('고궁명', '중국', '일본', '미국'))
    r_df = r_df.set_index('고궁명')
    
    print(r_df)
    r_df.plot(kind='bar', rot=50)
    plt.show()
    
if __name__ == "__main__":
    Gogo()
