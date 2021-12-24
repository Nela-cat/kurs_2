class People :
    def p(self):
        
        print(f"Name : {p1.name} , age : {p1.age} ,  id : {p1.id}")

a = (input('введите имя'))
e = (input('введите возраст'))
p = (input('введите вашу страну'))

p1=People()
p1.name=a
p1.age=e
p1.id=p
p1.p()





 


#class People :
 #   def __init__(self,name,age,place_of_birth):
  #      name : name
   #     age : age
    #    place_of_birth : place_of_birth
        
    #def info(self,n):
     #   for i in range(n):
      #      print(f"имя : {self.name}, М. р.: {self.place_of_birth}")

#a = (input('введите имя'))
#e = (input('введите возраст'))
#p = (input('введите вашу страну'))            
#p1=People(a,e,p)
#p1.info(1)


class Staz:
    def info(self,m):
        print(m-self.year)
           

p1=Staz()         
a = int(input('введите год с которого вы начали работать'))
p1.year=a
p1.info(2021)

         
    


