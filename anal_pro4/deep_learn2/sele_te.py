# --- daum 사이트에 접속하기
from selenium import webdriver
browser = webdriver.Chrome('C:/work/chromedriver') #   <== 브라우저 열기
browser.implicitly_wait(5)            #     <== 선택적인 명령으로 지정한 시간(초)동안 기다린다.
browser.get('https://daum.net')      #    <== 원하는 url을 적어 줌. 해당 사이트가 열린다.
browser.quit()                         #    <== 모든 작업을 끝내고 브라우저를 닫음