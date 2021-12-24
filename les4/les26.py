#class Human:
 #   def __init__(self,name,surname):
  #      self.name= name
   #     self.surname = surname
    #def hello(self):
     #   print(f"{self.name} , hello ")
        
#d1= Human('Nela','Genina')
#d1.hello()


#class Human:
     #def __init__(self,name,surname):
    #    self.name= name
   #     self.surname = surname
  #   def hello(self):
 #       print(f"{self.name} {self.surname} , hello ")



#class Student(Human):
 #   pass
#class Teacher(Human):
 #   pass

#s1 =Student('Renat','Dmit')
#s1.hello()



class Human:
     def __init__(self,name,surname):
        self.name= name
        self.surname = surname
        print('Human created')
     def hello(self):
        print(f"{self.name} {self.surname} , hello ")



class Student(Human):
    def study(self):
        print(f'{self.name} study')
class Teacher(Human):
    def teach(self):
        print(f"{self.name} teaches")

s1 =Student('Renat','Dmit')
s1.hello()        
s1.study()
s1.teach()
