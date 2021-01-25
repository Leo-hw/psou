# pandas 문제 6)
# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.
# Django 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.
#   project명 : django_test_pandas
#    1) 사번, 직원명, 부서명, 직급, 근무년수, 연봉을 DataFrame에 기억 후 출력하시오.
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
#    2) 부서명, 직급 자료를 이용하여  각각 급여합, 급여평균을 구하시오.
#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
#    4) 성별, 직급별 빈도표를 출력하시오.
# 
# 참고 : 원격 table 구조 얻기 > python manage.py inspectdb > a.py     


import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv
import matplotlib.pyplot as plt
