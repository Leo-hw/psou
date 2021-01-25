'''
사용자 정의 모듈을 연습해봅시다!
'''

print('뭔가를 하다가... 사용자 정의 모듈을 호출 시도')

import pack1.mymod1
list1 = [1,3]
list2 = [2,4]

pack1.mymod1.listHap(list1,list2)

def good():
    if __name__ == '__main__':
        print('최상위 메인 모듈은 나야 나')
        
good()

print('tot 는', pack1.mymod1.tot)
pack1.mymod1.kbs()

from pack1.mymod1 import mbc
mbc()

print()

from pack1etc.mymod2 import Hap, Cha
print('합은 ', Hap(5, 2))
print('차는 ', Cha(5, 2))

print('mymod3.py는 python path 폴더 중 어딘가에 저장한 상태')
from mymod3 import Gop
print('곱은 ', Gop(5, 2))

# 참고 : colab 에서 실습할 경우
#순서1)  mymod1.ipynb 파일을 작성 한 후 메뉴에서 '파일 ' -> .py 로 다운로드 한 후
#순서 2) form goolge.colab import files
#순서3) files

