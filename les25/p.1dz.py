#class People :
 #   def p(self):
        
  #      print(f"Name : {p1.name} , age : {p1.age} ,  id : {p1.id}")


        
#print('Введите "D" если хотите прекратить ')
#a = (input('введите имя'))
#e = (input('введите возраст'))
#p = (input('введите вашу страну'))

    
    
    

#p1=People()
#p1.name=a
#p1.age=e
#p1.id=p
#p1.p()






#class Staz:
 #   def info(self,m):
  #      print(m-self.year)
           

#p1=Staz()         
#oo = int(input('введите год с которого вы начали работать'))
##p1.year=oo
#p1.info(2021)



#while True:
 #   if a == "D":
  #      break
    
#while True:
#    if a == "D":
 #       break
#age = "How old are you?"
#while True:
 #   message = input(age)
    
  #  age1 = int(message)
   # if age1 <= 3:
    #    print("Cinema is free")
    #elif age1 <= 12:
     #   print("Cinema cost's 10$")
    #else:
    #    print("Cinema cost's 15$")





#while True:
 #   name = input("Введите имя: ")
  #  if name == "хватит":
   #     break
   # print("Привет ", name)



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

name= input('Введите ваше имя :  ')
age = (input('введите возраст : '))
place_of_birth = (input('введите вашу страну'))

class Anketa :
    def __init__(self,name,age,place_of_birth):
        self.name = name
        self.age = age
        self.place_of_birth =place_of_birth 
        name_check = re.search(r'[a]+e[b]+ d +', self.name)
        if name_check:
            print ('email valid')
        else:
            print ('email not valid')
            self.email = input("Enter your email: ")            
            sys.exit(0)
            
        
        
        
