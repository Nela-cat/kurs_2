class Animal :
    def __init__(self,name,age,place_of_birth,year,coming):
        self.name=name
        self.age = age
        self.place_of_birth=place_of_birth
        self.year=year
        self.coming=coming
        print('Animal created')
    def info(self):
        print(f" имя {self.name},возраст : {self.age}, М. р.: {self.place_of_birth}  , появление :{self.coming}"  )
         
class Poroda(Animal):
    def por(self):
        print(f"{self.name} porodn forest cat")
        
class Plase_of_residence(Animal):
    def plase(self):
        print(f"{self.name} у  нас дома")


        
h1=Poroda('Сирень',3,'ua',2018,'Found near the river')
h1.info()
h1.por()
h1=Plase_of_residence('Сирень',3,'ua',2018,'Found near the river')
h1.plase()



class Animal :
    def __init__(self,cat,dog,cow,tiger):
        self.cat=cat
        self.dog = dog
        self.cow=cow
        self.tiger=teger
        print('Animal created')
    def info(self):
        print(f" {self.cat}, {self.dog},  {self.cow}  , :{self.tigre.}"  )
         
class Sound(Animal):
    def s(self):
        print(f"{self.cat} : meow , {self.dog} ; woof , {self.cow} : muu , {self.tigre} : garrr")
        
class Plase_of_residence(Animal):
    def plase(self):
        print(f"{self.cat} : everywhere , {self.dog} ; everywhere , {self.cow} : everywhere , {self.tigre} : Africa")


        
h1=Sound('cat','dog','cow','tigre')
h1.info()
h1.s()
h1=Plase_of_residence('cat','dog','cow','tigre')
h1.plase()



class Animal :
    def __init__(self,name,age,place_of_birth,year,coming):
        self.name=name
        self.age = age
        self.place_of_birth=place_of_birth
        self.year=year
        self.coming=coming
        print('Animal created')
    def info(self):
        print(f" имя {self.name},возраст : {self.age}, М. р.: {self.place_of_birth}  , появление :{self.coming}"  )
         
class Poroda(Animal):
    def por(self):
        print(f"{self.name} porodn forest cat")
        
class Plase_of_residence(Animal):
    def plase(self):
        print(f"{self.name} у  нас дома")


        
h1=Poroda('Сирень',3,'ua',2018,'Found near the river')
h1.info()
h1.por()
h1=Plase_of_residence('Сирень',3,'ua',2018,'Found near the river')
h1.plase()
