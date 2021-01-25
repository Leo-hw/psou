# 예외처리 try ~ except
def divide(a,b):
    return a / b

print('뭔가를 하다가... ')

c = divide(5, 2)
#c = divide(5,0) # ZeroDivisionError: division by zero
print(c)

class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value
        

print('가자~~~Go')

try:
    c = divide(5, 2)
    #c = divide(5, 0)
    print(c)
    
    aa=[1,2]
    print(aa[0])
    #print(aa[2])
    
    #f = open('c:/work/aa.txt')
    f = open('c:/work/aaa.txt')
except ZeroDivisionError as e:
    print('err : 두 번째 숫자는 0 이면 안돼!!!' , e)
except IndexError:
    print('참조에러')
    
except Exception as e:
    print('에러 : ' + e)
finally:
    print('에러와 상관없이 반드시 수행')

print('프로그램 종료')

# exception 을 상속받은 NegtiveDivisionError 


