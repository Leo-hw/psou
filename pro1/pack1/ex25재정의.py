'''
메소드 오버라이드가 가능
'''
class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self):
        print('Child1에서 오버라이드')

class Child2(Parent):
    def printData(self):
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 동일하나 다른 기능을 갖는다.')
        
    def abc(self):
        print('Child2 클래스의 고유 메소드')
        
c1 = Child1()
c1.printData()
print()

c2 = Child2()
c2.printData()
c2.abc()

print('다형성 ----')
par = Parent()
par =c1
par.printData()

kbs = c1                    # 입력 자료에 의해 변수 타입이 결정된다는 점을 기억하자.

kbs.printData()

# 캐스팅이 필요 없음. 
# 객체 타입에 영향을 받지 않음 => 오버라이딩 된 메소드만 객체 타입으로 부르는 것이 아니라 그냥 부를 수 있음.// 자바와 구분되는 부분

kbs = c2
kbs.abc()
kbs.printData()
print()
plist = [c1,c2]
for i in plist:
    i.printData()