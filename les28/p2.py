#class Human:
 #   def __init__(self,name,surname,place_of_birth,yeat_of_birth):
  #      self.name=name
   #     self.surname=surname
    #    self.place_of_birth=place_of_birth
     #   self.year_of_birth=yeat_of_birth
    #def info(self):
     #   print(f"Name:{self.name}, surname : {self.surname}")
    #def year(self,years):
     #   return years-self.year_of_birth
#p1=Human('Nela', 'Genina',"ua =",2004)
#p1.info()
#print(p1.year(2022))

     
#2
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('person created')
    def info(self):
        
       
            
        print(f"name : {self.name} , age :{self.age}")

class Student(Human):
     def hello(self):
            print(f" student {self.name} hello")
     def study(self):
         print(f"Name student :{self.name} studing ")
        

class Teacher(Human):
    
    def teach(self):
        
        def hello(self):
           print(f" student {self.name} hello")
           #print(f"name teache : {self,.name} teaches")
        

s1 = Student('Nela', '17')
s1.info()
s1.study()
s1.hello()



class Student(Human): # переопределение  <-----
    def __init__(self,name,age,crs,mark):
        Human.__init__(self,name,age)
        self.crs=crs
        self.mark=mark
    def hello(self):
        print(f" student {self.name} hello   ")
    def study(self):
        print(f"Name student :{self.name} studing  ")
    def studing(self):
        print(f"curs : {self.crs} , mark : {self.mark}")

s1 = Student('Nela', '17' , '1' , 5)
s1.info()
s1.study()
s1.studing()
            







