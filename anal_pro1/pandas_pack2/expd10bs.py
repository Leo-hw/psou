import requests  
from bs4 import BeautifulSoup

def go():
    base_url = "http://www.naver.com/index.html"
    
    #storing all the information including headers in the variable source code
    source_code = requests.get(base_url)
    
    #sort source code and store only the plaintext
    plain_text = source_code.text
    
    #converting plain_text to Beautiful Soup object so the library can sort thru it
    convert_data = BeautifulSoup(plain_text, 'lxml')
    
    for link in convert_data.findAll('a'):
        href = base_url + link.get('href')  #Building a clickable url
        print(href)                          #displaying href

go()