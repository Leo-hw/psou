'''
'''

class Animal():
    def move(self):
        print('동물은 뛰어댕김')

class Dog(Animal):
    name = "댕댕이"
    
    def move(self):
        print("댕댕이는 총총")

class Cat(Animal):
    name = "고양이"
    
    def move(self):
            print('고양이는 쭈으으으욱')
            
class Wolf(Dog, Cat):
    pass
    
class Fox(Cat, Dog):
    def move(self):
        print('여우는 한번에 두발씩 뜀')
        
    def foxtMethod(self):
        print('여우는 어떻게 우나? What the Fox say 링딩딩딩디리리링 ')
        
a1 = Animal()
d1 = Dog()
c1 = Cat()
w1 = Wolf()
f1 = Fox()

a1.move()
d1.move()
c1.move()
w1.move() 
f1.move()
f1.foxtMethod()   
print('*'*20)
ani = {a1,d1,c1,w1,f1}
for a in ani:
    a.move()
    