import math
class Pif :
    
    
    def __init__(self,a,b):
        self.a = a
        self.b=b
        
    def s_c(self):
        if a >b :
            print(f" if gep a={a} , kat b={b}  kat c = {math.sqrt((self.a**2)-(self.b**2))}")
        else:
            print('a должно быть > b')

    def s_b(self):
        print(f" if kat a={a} ,kat b={b} gep c = {math.sqrt((self.a**2)+(self.b**2))}")

         
       
        
a=int(input("введите  a"))
b=int(input("введите  b"))
c1=Pif(a,b)
c1.s_c()

c2=Pif(a,b)
c2.s_b()

  
