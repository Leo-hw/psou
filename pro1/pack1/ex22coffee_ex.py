'''
커피 자판기 문제
입력 자료는 키보드를 사용
커피는 한 잔에 200원
100원 넣고 커피를 요구하면 요금 부족 메시지 출력
400원 넣고 2잔 요구하면 두잔 출력
500원 넣고 1잔 요구하면 300원 반납

출력 형태 ---------------------
동전을 입력하세요 : 400
몇 잔을 원하세요 ; 2
커피 2잔과 잔돈 0원
'''
class Machine():
    def __init__(self):
        self.coffee = coinin()
        
    def showData(self):
        self.coin = int(input('동전을 입력하세요:')) 
        if self.coin >= 200:
            self.cupcount = int(input('몇잔을 원하세요:'))
            self.coffee.calc(self.coin, self.cupcount)
        else:
            print('요금 부족')
        
class coinin():
    
    def calc(self,coin, cupcount):
        self.price = 200 * cupcount
        if self.price <= coin: 
            self.change = coin - self.price
            print('커피 ' , cupcount , ' 잔 과 잔돈 ' , self.change ,' 원')
        else:
            print('요금 부족')

    
if __name__ == "__main__":
    Machine().showData()

    