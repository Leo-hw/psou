'''
다른 클래스의 멤버로 사용될 핸들 클래스 
'''
class PohamHandle:
    quantity = 0
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
        