# 다중 상속이 가능
class Tiger:
    data = '호랑이 세상'
    
    def Cry(self):
        print('호랑이 : 어흥')
        
    def Eat(self):
        print('맹수니까 고기를 좋아함?')
        
class Lion:
    def Cry(self):
        print('사자: 으르렁')
        
    def Hobby(self):
        print('백수의 왕은 낮잠을 즐겨함.')
        
class Liger1(Tiger, Lion):              # 다중 상속은 순서가 중요하다
    pass

a1 = Liger1()
a1.Cry()            # 얘는 앞에 상속받는 객체의 메소드를 우선으로 둠
a1.Hobby()
a1.Eat()
print(a1.data)


print('*'*15)
class Liger2(Lion, Tiger):
    data = '라이거 만세'
    
    def play(self):
        print('라이거 고유 메소드')
        self.Hobby()
        super().Hobby()
        print(self.data)
        print(super().data)
        
    def Hobby(self):
        print('라이거는 초원을 걸으며 사색을 즐김')
        
        
a2 = Liger2()
a2.Cry()
a2.Eat()
a2.Hobby()
a2.play()
print()
print(Liger2.__mro__)           # 클래스 탐색 순서
