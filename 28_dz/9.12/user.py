class User :
    def __init__(self, first_name,last_name,age,place_of_birth):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place_of_birth=place_of_birth
        self.login_attempts = 0
    def describe_user(self):
        print(f"Nmae : {self.first_name} , last name : {self.last_name} , age : {self.age} , plase of dirth : {self.place_of_birth}")
    def greeting_user(self):
        print(f"Hello {self.first_name} ")


    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f" login attempts : {self.login_attempts}")


    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f" reset login attempts  : {self.login_attempts}")    
