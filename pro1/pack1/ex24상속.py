# 상속
class Person:
    say  = '난 사람이야~~~'
    nai = '20'
    __kbs = 'good'      # private member 멤버 변수 = 현재 클래스에서만 호출이 가능.
    
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
        
    def PrintInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
    
    def Hello(self):
        print('안녕')
        print('Hello 에서 kbs 출력' , self.__kbs)
        
    @staticmethod
    def sbs(tel):
        print('sbs - static method :', tel)
        #print(self.say)             # 클래스 멤버 호출 불가. 해당 클래스 멤버에 상관없는 독립적 처리에 사용.
    
    @classmethod
    def ytn(cls):
        print('Person이 가진 ytn 메소드', cls.say, cls.nai)       # cls 로 멤버 변수에 접근이 가능.
    
p = Person('22')
p.PrintInfo()
p.Hello()

print('----'*20)
class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'
    
    def __init__(self):
        print('Employee 생성자')
        
    def PrintInfo(self):        # method override
        print('Employee 메소드')
        
    def EprintInfo(self):
        self.PrintInfo()
        super().PrintInfo()
        print(self.say, super().say)
        self.Hello()
        super().Hello()
        
e = Employee()
print(e.say, e.nai, e.subject)
e.PrintInfo()
e.EprintInfo()

print(' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)           #BoundMethod call #부모 생성자 호출 시 순서는 상관 없다.
        
    def WprintInfo(self):
        self.PrintInfo()
        super().PrintInfo()
        
w = Worker('25')
print(w.say, w.nai)
w.PrintInfo()
w.WprintInfo()

print('***'*20)

class Programmer(Worker):
    def __init__(self, nai):
        print('프로그래머 생성자')
        #super().__init__(nai)   # BoundMethod call
        Worker.__init__(self, nai) # UnBoundMethod call
        
    def WprintInfo(self):           # overrride
        print('Programmer 클래스에서 Worker의 메소드를 오버라이딩 ')
    
    def abc(self):
        print('Programmer Hello 에서 kbs 출력' , self.__kbs)

pr = Programmer(33)
print(pr.say, pr.nai)
pr.PrintInfo()
pr.WprintInfo()

print('클래스 타입 확인')
a = 10
print(type(a))
print(Person.__base__) # 현재 클래스의 부모 클래스 타입 확인
print(Employee.__base__) 
print(Programmer.__base__)
#pr.abc()    # AttributeError: 'Programmer' object has no attribute '_Programmer__kbs'
pr.sbs('010-1111-2222')         #객체 변수 이름으로 부르지 말고, 클래스 이름으로 불러라.( 가능은 하지만 비 권장)
Person.sbs('010-222-3333')  # 권장 
Person.ytn()
        