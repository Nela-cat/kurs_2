class Machin:
    def __init__(self,mark,name,time,speed,user):
        self.mark = mark
        self.name= name
        self.time=time
        self.speed = speed
        self.user=user
        print('machine created')
        
class Roket(Machin) :
    def info(self):
        print(f"Roket:\n\t mark:{self.mark}\n\t name:{self.name}\n\t time:{self.time}\n\t speed:{self.speed} ")
    def infor_user_1(self):
        print(f'{self.user} flies to mars ,  time : {self.time} , speed :{self.speed}')
    
class Boeing(Machin):
    def info_b(self):
        print(f"Boeing:\n\t mark:{self.mark}\n\tname:{self.name}\n\ttime:{self.time}\n\tspeed:{self.speed} ")
    def info_user_2(self):
        print(f'{self.user} going to Cuba')    


while True :
    n  = int(input('Enter 1 if you want to rocket into space and 2 if you want to Cuba'))
    if n == 1 :
       f = Roket('Vanguard', 'USA' , 12 , 1200  , 'Nela')
       f.info()
       f.infor_user_1()
    elif n ==2 :
       f = Boeing('Lexus', 'USA' , '3 year' , 120 , 'Nela')
       f.info_b()
       f.info_user_2()

h1=Roket('Vanguard', 'USA' , 12 , 1200 , 'Nela')
f.info()
f.infor_user_1('Vanguard', 'USA' , '1958' , 1200 , 'Nela')
h1=Boeing('boing', 'nurt' , '3 year' , 120 , 'Nela')
f.info_b()
f.info_user_2('boing', 'nurt' , '3 year' , 120 , 'Nela')
