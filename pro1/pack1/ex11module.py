'''
Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리하는 단위
하나의 파일은 모듈 단위로 저장되고 관리한다.
표준 모듈, 사용자 작성 모듈, 써드파티(third party)모듈
'''
# 내장된 모듈 경험하기 
print('뭔가를 하다가 ...')
import sys
print(sys.path)
# sys.exit()      #프로그램의 강제 종료

import math
print(math.pi)

print('뭔가를 하다가 ...')
import calendar
calendar.setfirstweekday(6) #일요일을 처음으로
calendar.prmonth(2020,10)

print()
import random                                # 모듈을 로딩
print(random.random())
print(random.randint(1,10))

# from 모듈 import 멤버명
from random import random       #모듈의 멤버를 로딩
#from random import *
print(random())

print('프로그램 종료')
