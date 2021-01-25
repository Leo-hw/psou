'''
클래스로 새로운 타입 생성 ; Singer
'''

class Singer:
    title_song = '가을이 가네'           # 멤버 변수 - 전역
    
    def sing(self):
        msg = '노래는'                        # 지역
        print(msg, self.title_song, '☆☆☆')
        
bts = Singer()
bts.sing()

print()
blackpink = Singer()    
blackpink.sing()

print()
bts.co = '빅히트'
print('소속사 : ' + bts.co)
#print('소속사 : ' + blackpink.co) # AttributeError: 'Singer' object has no attribute 'co'

print(id(bts), id(blackpink))


