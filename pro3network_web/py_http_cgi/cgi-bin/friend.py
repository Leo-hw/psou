'''
client 가 입력 한 데이터를 접수
'''
import cgi 

form = cgi.FieldStorage()           # dict type 으로 자료 받음

name = form['name'].value       # java : request.getParamete("name")
tel = form['phone'].value       
gender = form['gender'].value       

print('Content-Type:text/html;charset=utf-8\n')
print(form['name'].value)
print('''
<html>
<body>
가나다

이름은 {0}, 전화는 {1} <br> 성별은 {2}

</body></html>    
    '''.format(name, tel, gender))