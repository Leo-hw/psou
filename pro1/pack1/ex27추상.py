# 추상 클래스 : 추상 메소드를 하나 이상 가진 경우에만 해당됨

from abc import*

class AbstractClass(metaclass = ABCMeta):       # 추상 클래스
    name='난 AbstractClass'
    @abstractmethod
    def abcMethod(self):        # 추상 메소드
        pass
    
    def normalMethod(self):     #일반 메소드
        print('추상 클래스 내의 일반 메소드')
        
        
#parent = AbstractClass()    #err :Can't instantiate abstract class AbstractClass with abstract methods abcMethod

class Child1(AbstractClass):
    name = '난 Child1'
    
    def abcMethod(self):            # 반드시 오버라이딩 해야함
        print('추상메소드를 일반 메소드로 오버라이딩')
    

class Child2(AbstractClass):
    def abcMethod(self):            # 반드시 오버라이딩 해야함
        print('추상메소드를 Child2에서 오버라이딩')
    
    def normalMethod(self):      # 오버라이딩 선택적
        print('추상 클래스의 일반 메소드를 재정의 함')

c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print()
c2 = Child2()
print(c2.name)
c2.abcMethod()    
c2.normalMethod()

# 추상 클래스 타입의 변수 선언은 가능
parent = AbstractClass
print(type(parent))
print()

parent = c1
parent.abcMethod()
print()
parent = c2
parent.abcMethod()

print('\n\n 추상 연습2-------------------------')
class Friend(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def hobby(self):
        pass
    
    def printName(self):
        print('이름은~ ' + self.name)
        
class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + '거리를 걸어다님')
        
    def printAddr(self):
        print('주소는 ' + self.addr)
        
class Chris(Friend):
    def __init__(self, name, addr, age):
        Friend.__init__(self, name)
        self.addr = addr
        self.age = age
        
    def hobby(self):
        print(self.addr +'동네를 뛰어댕김')
        print(self.addr  + '살고 있으니까 , 나이는' +\
               str(self.age) +\
                '살 임을 참고로 알림!')
        
john = John('존', '역삼동')
john.printName()
john.hobby()
john.printAddr()

print('------------------------')
chris = Chris('크리스', '신사동', 23)
chris.printName()
chris.hobby()
    
