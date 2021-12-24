class Animal :
    def __init__(self,cat,dog,cow,tiger):
        self.cat=cat
        self.dog = dog
        self.cow=cow
        self.tiger=tiger
        print('Animal created')
    def info(self):
        print(f"  {self.cat},{self.dog}, {self.cow}  , {self.tiger}"  )
         
class Poroda(Animal):
    def por(self):
        print(f"{self.name} porodn forest cat")
        
class Sound(Animal):
    def s(self):
        print(f"{self.cat} : meow , {self.dog} ; woof , {self.cow} : muu , {self.tiger} : garrr")
        
class Plase_of_residence(Animal):
    def plase(self):
        print(f"{self.cat} : everywhere , {self.dog} ; everywhere , {self.cow} : everywhere , {self.tiger} : Africa")


        
h1=Sound('cat','dog','cow','tiger')
h1.info()
h1.s()
h1=Plase_of_residence('cat','dog','cow','tiger')
h1.plase()
