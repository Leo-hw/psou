'''
클래스
'''
#모듈과 클래스의 네임을 같게 하는 것을 권장하지 않지만 가능함.

kor = 100
def abc():          
    print('모듈의 함수')
    
class MyClass():
    kor = 90                # 권장하지 않음
    
    def abc(self):          
        print('난 메소드야')
        
    def show(self):
        #kor = 80
        print(self.kor)
        print(kor)      # 현재 메소드를 검색하고 없으면 모듈의 멤버를 참조 ( 여기서  kor 이 없을 경우 더 상위의 멤버를 찾음)
        self.abc()
        abc()               # 모듈의 함수 호출
        
myclass = MyClass()
myclass.show()

print('~~~~~'*20)
class My:
    a = 1
print(My.a)
my1 = My()
print(my1.a)

my2 = My()
print(my2.a)
my2.b = 2
print(my2.b)    

#print(my1.b)    #AttributeError: 'My' object has no attribute 'b'
#print(My.b)      #AttributeError: type object 'My' has no attribute 'b'
    
    