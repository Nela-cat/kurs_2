class User:
    def __init__(self, first_name,last_name,age,place_of_birth):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place_of_birth=place_of_birth
    def describe_user(self):
        print(f"Nmae : {self.first_name} , last name : {self.last_name} , age : {self.age} , plase of dirth : {self.place_of_birth}")
    def hello(self):
        print(f"Hello {self.first_name} ")


class Admin(User):
    def __init__(self, first_name,last_name,age,place_of_birth):
        User.__init__(self, first_name,last_name,age,place_of_birth)
        self.privileges = []
        
    def show_privileges(self):
        for p in self.privileges:
            print(f"Admin : {p}")



        

u1 = User('Nela' , 'Genina' , 17 , 'Ua')
u1.describe_user()
u1.hello()

u2= User('Anna' , 'Tar' , 13 , 'USA')
u2.describe_user()
u2.hello()

admin = Admin('Anelia' , 'Genina' , 17 , 'Ua')
admin.privileges = [' зрешено доб. сооб.',' раз. банить',' раз. удалять пользователя']
admin.show_privileges()
