# 시각화 모듈
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지

# %matplotlib inline                          ipython 기반
'''
#x = [0,1,2]
#x = ['서울', '인천','천안']
x = ('서울', '인천','천안')
#x = {'서울', '인천','천안'} set 은 안됨(순서가 없기 때문에.)
# list 와 tuple 은 가능(순서가 있다)

y = [5,3,7]

plt.xlim([-1,3])
plt.ylim([0,10])
plt.yticks(list(range(0,11,3)))     # 인위적으로 라벨을 조정

#plt.scatter(x,y)
plt.plot(x, y)
plt.show()
'''
'''
data = np.arange(1,11,2)
print(data)
plt.plot(data)
x = [0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(a,b, str(b))

plt.show()

plt.plot(data)
plt.plot(data, data, 'r')
for a, b in zip(data,data):
    plt.text(a,b,str(b))
plt.show()
    
plt.show()
'''
'''
# 사인 곡선
x = np.arange(10)
y = np.sin(x)
print(x,y)
#plt.plot(x,y, 'bo')             # style 'bo' 파랑 동그라미
#plt.plot(y, 'r+')
plt.plot(x,y, 'go--', marker="o", ms=15, mec='g', mew=5, mfc='r')

plt.show()
'''
'''
# hold : 복수의 plot 명령을 하나의 그림에 겹쳐서 출력
x = np.arange(0, np.pi*3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('sin & cosine')
plt.legend(['sin','cosine'])
plt.show()
'''
'''
# subplot : Figure 를 여러 개의 영역으로 분리
x = np.arange(0, np.pi*3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('sine')

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine')
plt.show()
'''
# 꺽은 선 그래프(차트)를 그린 후 이미지를 파일로 저장.
irum = ['a','b','c','d','e']
kor = [80,90,70,70,90]
eng = [40,70,80,70,60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs--')
plt.ylim([30,100])
plt.title('시험 점수')
plt.legend(['국어','영어'], loc= 1)
plt.grid(True)

# 차트를 이미지로 저장
fig = plt.gcf() # 저장 준비

plt.show()
fig.savefig('plot1.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)
plt.show()
