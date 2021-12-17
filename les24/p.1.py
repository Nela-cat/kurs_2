#ООП
#class Human :
 #   name : Den
  #  surname : Dmitriev
   # age : 24
    #place_of_birth : UA

#class Human :
 #   def info(self,n):
  #      for i in range(n):
           # print(f"имя : {self.name},фамилия : {self.surname}, М. р.: {self.place_of_birth}")

#p1=Human()
#p1.name='Nela'
#p1.surname='Genina'
#p1.place_of_birth='UA'

#p2=Human()
#p2.name='Miha'
#p2.surname='Oksanic'
#p2.place_of_birth='UA'

#p1.info(5)  # n=5
#p2.info(4)

#print(f"имя : {p1.name},фамилия : {p1.surname}, М. р.: {p1.place_of_birth}")
#print(f"имя : {p2.name},фамилия : {p2.surname}, М. р.: {p2.place_of_birth}")




#class Human :
 #   def rez_year( self , m ):
  #      print( m - self.year)
           
       
#p1=Human()
#p1.name='Nela'
#p1.surname='Genina'
#p1.place_of_birth='UA'
#p1.year= 2004

#p2=Human()
#p2.name='Miha'
#p2.surname='Oksanic'
#p2.place_of_birth='UA'
#p2.year=2004

#print(p1.rez_year(2021))






#4
  
class Human :
    def __init__(self,name,surname,place_of_birth,year):
        self.name=name
        self.surname=surname
        #self.age = age
        self.place_of_birth=place_of_birth
        self.year=year

    
    def info(self,n):
        for i in range(n):
            print(f"{self.name},фамилия : {self.surname}, М. р.: {self.place_of_birth}")
  
    
    #def rez_year( self , m ):
        #print( m - self.year)
           
       
p1=Human('Nela','Genina','ua',2004)
#p1.name='Nela'
#p1.surname='Genina'
#p1.place_of_birth='UA'
#p1.year= 2004

p2=Human('Dana','Genina','ua',2004)
#p2.name='Miha'
#p2.surname='Oksanic'
#p2.place_of_birth='UA'
#p2.year=2004

#p1.info(5)  # n=5
#p2.info(4)

#print(p1.rez_year(2021))
p1.info(1)

    

