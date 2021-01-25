 # --- daum 사이트에 접속하기
# from selenium import webdriver
# browser = webdriver.Chrome('C:/work/chromedriver') #   <== 브라우저 열기
# browser.implicitly_wait(5)               #  <== 선택적인 명령으로 지정한 시간(초)동안 기다린다.
# browser.get('https://www.accuweather.com/es/bo/uyuni/35226/december-weather/35226') #         <== 원하는 url을 적어 줌. 해당 사이트가 열린다.
# browser.quit()                             #<== 모든 작업을 끝내고 브라우저를 닫음

 # --- 크롬 드라이버 실행 후 검색 하기 
import time
from selenium import webdriver
browser = webdriver.Chrome('C:/work/chromedriver')  #Optional argument, if not specified will search path.
browser.get('https://www.accuweather.com/es/bo/uyuni/35226/december-weather/35226');
time.sleep(5)          # Let the user actually see something!
subjects = browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[2]/div/div[2]/a[20]/div[1]/')
#browser.find_elements_by_css_selector('body > div >  div.icon-container > img')
# body > div > div.two-column-page-content > div.page-column-1 > div.content-module > div.monthly-component.non-ad > div > div.monthly-calendar > a:nth-child(21) > div.monthly-panel-top > div.icon-container > img
#body > div > div.two-column-page-content > div.page-column-1 > div.content-module > div.monthly-component.non-ad > div > div.monthly-calendar > a:nth-child(14) > div.monthly-panel-top > div.icon-container > img
print('subjects : ', subjects)
print('1')
for subject in subjects :
    print('2')
    print( subject.text )
    browser.quit()       #or   driver.close()



# search_box = browser.find_element_by_name('q')
# search_box.send_keys('검색단어')
# search_box.submit()
# time.sleep(5)          # Let the user actually see something!
# browser.quit()
# browser.find_element_by_name()
# browser.find_element_by_xpath()

# #연습 : Daum 로그인
# from selenium import webdriver
# browser = webdriver.Chrome('C:/work/chromedriver')
# browser.implicitly_wait(5)
# browser.get( 'https://logins.daum.net/accounts/signinform.do' ) 
# browser.find_element_by_id('id').send_keys('본인id')
# browser.find_element_by_id('inputPwd').send_keys('본인pwd')
# browser.find_element_by_id('inputPwd').clear()     # clear text
# browser.find_element_by_id('loginBtn').click()

# # 메일 읽어오기
# browser.implicitly_wait(5)
# browser.get('https://mail.daum.net/')
# subjects = browser.find_elements_by_css_selector('strong.tit_subject')
# print('subjects : ', subjects)
# 
# for subject in subjects :
#     print( subject.text )
#     driver.quit()       #or   driver.close()
#  
# # 이클립스 또는 jupyter lab으로 실행해 보기  : 화면 캡처
# 
# from selenium import webdriver
# try:
#     url = "http://www.daum.net"
#     browser = webdriver.Chrome('C:/work/chromedriver')
#     browser.implicitly_wait(3)
#     browser.get(url);
#     browser.save_screenshot("daum_img.png")
#     browser.quit()
#     print('성공')
# 
# except Exception:
#     print('에러')
