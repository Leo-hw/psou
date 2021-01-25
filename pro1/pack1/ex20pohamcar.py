# 클래스의 포함 관계 - 핸들 클래스를 별도 작성 후 호출
from pack1.ex20handle import PohamHandle

class PohamCar:
    turnShow = '정지'
    
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle()         # 클래스의 포함.
    
    def TurnHandle(self, q):                    # 여기서 먼저 값을 가지고, if 문에 따라 분류 하고, 포함 관계에 있는 클래스로 넘어감.
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        elif q<0:
            self.turnShow = self.handle.LeftTurn(q)    
        elif q == 0:
            self.turnShow = '직진'


if __name__ == '__main__':
    tom = PohamCar('tom')
    tom.TurnHandle(20)
    print(tom.ownerName + '의 회전량은 '+ tom.turnShow+ str(tom.handle.quantity))
    
    tom.TurnHandle(-20)
    print(tom.ownerName + '의 회전량은 '+ tom.turnShow+ str(tom.handle.quantity))
        
    print()
    john = PohamCar('john')
    john.TurnHandle(0)
    print(john.ownerName + '의 회전량은 '+ john.turnShow+ str(john.handle.quantity))
    
    
    
    