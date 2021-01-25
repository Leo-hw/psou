'''
Module 의 멤버 중 class 의 이해(객체 운영)
클래스의 멤버로 메소드와 변수
접근지정자 없다. 
메소드 오버로딩 없다.
다중 상속 가능. 자바의 interface - X
'''
print('무언가를 하다가~ oop 를 사용하고 싶다면~?')
print('그 때 클래스가 나오는거지')
class TestClass:
    aa = 1 # 멤버 변수(TestClass) - Global(전역) - prototype
    
    def __init__(self):                 # 얘가 생성자
        print('생성자')
        
#     def __del__(self):                  # 얘는 소멸자~ // 거의 사용되지 않음. 여기도 가컬이 존재 Garbage collector
#         print('소멸자')
        
    def myMethod(self):
        name = '한국인'
        print(name)
        print(self.aa)

print('class의 멤버변수 aa : ', TestClass.aa)
#TestClass.myMethod(self) 
# 원형클래스도 사용은 가능하지만 원형 클래스는 다른 클래스를 사용하기 위한 매개체(?)

test = TestClass()                  # 생성자 호출. TestClass type 의 객체가 생성
print(test.aa)
test.myMethod()

print('\n 메소드 호출 방법')
TestClass.myMethod(test)        #방법1 : UnBound Method Call
test.myMethod()                          #방법2 : Bound Method Call

print('클래스 타입 : ', isinstance(test, TestClass))     # True

print()
print(type(1))
print(type(test))
print(id(test), id(TestClass))

print('\n\n클래스 연습 2 ')
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = '킬로미터'             # 지역변수(메소드 내에서만 유효.)
        msg = '속도:' + str(self.speed) + km
        return msg

print(Car.handle, Car.speed)

car1 = Car('paul', 10)
print(car1.handle, car1.name, car1.speed)
car1.color = '검정'               # car1 객체에 color 변수 추가.
print(car1.color)

#print(Car.color)    # AttributeError : type object 'Car' has no attribute 'color'

print()
car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)
#print(car2.color)     # AttributeError: 'Car' object has no attribute 'color'

print('주소 출력 : ', Car, car1, car2)
print('주소 출력 : ', id(Car), id(car1), id(car2))

print(car1.__dict__)        # 각 객체의 멤버 확인
print(car2.__dict__)

print('메소드 호출')
print('car1 => ', car1.showData())
print('car2 => ', car2.showData())

print(car1.speed)
print(car2.speed)
        
                
        