class User:
    def __init__(self, first_name,last_name,age,place_of_birth):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place_of_birth=place_of_birth
        self.login_attempts = 0

        
    def describe_user(self):
        print(f"Nmae : {self.first_name} , last name : {self.last_name} , age : {self.age} , plase of dirth : {self.place_of_birth}")
    def hello(self):
        print(f"Hello {self.first_name} ")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f" login attempts : {self.login_attempts}")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f" login attempts 2 : {self.login_attempts}")


u1 = User('Nela' , 'Genina' , 17 , 'Ua')
u1.describe_user()
u1.hello()

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()


u1.reset_login_attempts()
u1.reset_login_attempts()



u2= User('Anna' , 'Tar' , 13 , 'USA')
u2.describe_user()
u2.hello()

