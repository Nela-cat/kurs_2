class Car :
    def __init__(self,mark,model,year):
       self.mark=mark
       self.model=model
       self.year=year
       self.adometr = 0
        
    def get_desk_name(self):
        print(f"mark :{self.mark} , model : {self.model} , year : {self.year} ")
    def rid_ad(self):
        print(f"  моя машина {self.mark}  имееь значение пробега {self.adometr}")

    def abdate_adometr(self,n):
        if n >= self.adometr :
            self.adometr=n
            print(f'{self.adometr}')
        else:
            print('пробег ски не возможно')

    def inkriment_ad(self,m):
        self.adometr += m
        print(f'новый пр : {self.adometr}'  )
        
class Electro_car(Car):
    def __init__(self,mark,model,year,batarea):
        
        Car.__init__(self,mark,model,year)       
        self.batarea=0

    def info(self):
        print(f"mark :{self.mark} , model : {self.model} , year : {self.year} ,batarea {self.batarea}  ")

    def bat_el(self,b):
        self.batarea=b
        print(f'batarea : {self.batarea}'  )

    def cois(self,c):
        if c>=1000000:
            print(f'машина ваша')
            
        else :
            print('no  не меньше {c}')
        
        
        
    
        

        


p1 = Car('BMW' , '24 rav' , 2000  )
n = int(input('n='))
m = int(input('m='))
p1.adometr = 23
p1.get_desk_name()
p1.abdate_adometr(n)
p1.rid_ad()
p1.inkriment_ad(m)

P=Electro_car('RAV' , '24 rav' , 2000 ,23)
b = int(input('b='))
c=int(input(' введите кол денег'))
P.info()
P.bat_el(b)
P.cois(c)



 
