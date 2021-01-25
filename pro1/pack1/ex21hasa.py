'''
로또 번호 출력 : 클래스의 포함 연습
'''

import random

class lottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(lottoBall(i))      # 클래스의 포함 관계(로또 볼의 생성자를 부르면서 i 를 집어넣음)
     
     
    def selectBalls(self):
        # 섞기 전 출력
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        
        random.shuffle(self.ballList)
    
        # 섞은 후 출력
       
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        print()
        return self.ballList[0:6]
            
class LottoUi :
    def __init__(self):
        self.machine = LottoMachine()           # 클래스의 포함 관계
        
    def playLotto(self):
        input("로또를 뽑으려면 엔터키를 누르세요!!!!!!")
        selectBalls = self.machine.selectBalls()
        for ball in selectBalls:
            print("%d"%(ball.num))
if __name__ == '__main__':
    LottoUi().playLotto()    
        