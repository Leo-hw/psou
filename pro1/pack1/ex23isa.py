'''
클래스의 상속
'''

class Animal:
    age = 0
    
    def __init__(self):
        print('Animal 생성자')
    
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal):              # 클래스의 상속
    def my(self):
        print('댕댕이라 불러주오')
        
dog1 = Dog()
dog1.move()
dog1.my()
print(dog1.age)

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()
        