class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound=sound
    def info(self):
        print(f" вид животного  :{self.species}")
    def animal_sound(self):
        print(f" sound  : {self.sound}")
        



class Dog(Animal):
    def __init__(self,species,sound,name):
        Animal.__init__(self,species,sound)
        self.name=name
    def name_animal(self):
        
        print(f"{self.species} name {self.name}")
        print(f" +-------------+")
        
class Cat(Animal):
    def __init__(self,species,sound,name):
        Animal.__init__(self,species,sound)
        self.name=name
    def name_animal(self):
        print(f"{self.species} name {self.name}")
        
    
        
animal=  Animal('animal' , 'grrrrr')
animal.info()
animal.animal_sound()

animal2=Dog('dog' , 'waf-waf','Polo')
animal2.info()
animal2.animal_sound()
animal2.name_animal()

animal3=Cat('cat' , 'my' , 'Bell')
animal3.info()
animal3.animal_sound()
animal3.name_animal()
        
