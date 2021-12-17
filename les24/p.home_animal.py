#5
class Animal :
    def __init__(self,name,age,place_of_birth,year,coming):
        self.name=name
        self.age = age
        self.place_of_birth=place_of_birth
        self.year=year
        self.coming=coming

    
    def info(self,n):
        for i in range(n):
            print(f" имя {self.name},возраст : {self.age}, М. р.: {self.place_of_birth}  , появление :{self.coming}"  )
  
    
    #def rez_year( self , m ):
        #print( m - self.year)
           
       
p1=Animal('Сирень',3,'ua',2018,'Found near the river')
#p1.name='Сирень'
#p1.age=3
#p1.place_of_birth='UA'
#p1.year= 2018
#p1.coming= 'Found near the river'



#print(p1.rez_year(2021))
p1.info(3)    
