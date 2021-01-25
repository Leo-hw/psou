from selenium import webdriver
 

try:

    url = "http://www.daum.net"

    browser = webdriver.Chrome('C:/work/chromedriver')

    browser.implicitly_wait(3)

 

    browser.get(url);

    browser.save_screenshot("daum_img.png")

    browser.quit()

 

    print('성공')

except Exception:

    print('에러')
browser = webdriver.Chrome('C:/work/chromedriver')

browser.implicitly_wait(5)

browser.get( 'https://logins.daum.net/accounts/signinform.do' ) 

browser.find_element_by_id('id').send_keys('본인id')

browser.find_element_by_id('inputPwd').send_keys('본인pwd')

browser.find_element_by_id('inputPwd').clear()     # clear text

browser.find_element_by_id('loginBtn').click()
