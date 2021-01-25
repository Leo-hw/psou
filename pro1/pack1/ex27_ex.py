# 문제풀기
from abc import *

class Employee(metaclass = ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print(self.irum, self.nai)

class Temporary(Employee):
    
    def __init__(self,irum, nai, ilsu, ildang):
        self.irum=irum
        self.nai=nai
        self.ilsu=ilsu
        self.ildang = ildang
         
    def pay(self):
        self.donTem = self.ilsu * self.ildang       
        return self.donTem
    
    def data_print(self):
        print('이름: ', self.irum, '  나이 : ', self.nai, '  월급 : ', self.pay())
        
class Regular(Employee):
    def __init__(self,irum,nai, salary):
        self.irum=irum
        self.nai=nai
        self.salary = salary
        
    def pay(self):
        pass
        
    def data_print(self):
        print('이름 : ', self.irum, '  나이 : ', self.nai,'  급여 : ', self.salary)
        
class Salesman(Regular):
    def __init__(self,irum, nai, salary, sales, commission):
        Regular.__init__(self, irum, nai, salary)
        self.sales = sales
        self.commission = commission
        self.suSales = self.salary + sales * commission
      
      
    def data_print(self):
        print('이름 : ',self.irum, '  나이 : ', self.nai, '  수령액 : ', self.suSales)
        
        
t = Temporary('홍길동', 25,20,15000)
r = Regular('한국인', 27, 350000) 
s = Salesman('손오공', 29, 120000, 500000, 0.25)
t.data_print()
r.data_print()
s.data_print()        