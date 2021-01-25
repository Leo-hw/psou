'''
has a 관계
    - 실제로는 클래스는 다른 곳에 만들어 둬야함.
클래스의  포함 : 냉장고 클래스에 음식물 클래스 담기
'''

class FoodData():
    def __init__(self, irum, expiry_date):
        self.irum = irum
        self.expiry_date = expiry_date

class Fridge:
    isOpened = False            # 냉장고 문 개폐 여부.
    foods = []
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')
    
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)    # 포함관계
            print('냉장고 속에 음식이 들어감')
            self.list()
        else:
            print('냉장고 문이 닫혀서 음식을 넣을 수 없음')
    
    def close(self):    
        self.isOpened = False
        print('냉장고문 닫기')
     
    def list(self):     # 냉장고 속 내용물 확인
        for f in self.foods:
            print('-', f.irum, f.expiry_date)
        print()

f = Fridge()
apple = FoodData('사과', '2020-12-20')

f.put(apple)

f.open()
f.put(apple)
f.close()

print()

cola = FoodData('콜라', '2022-1-20')
f.open()
f.put(cola)
f.close()
