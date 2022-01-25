from user import *
class Admin(User):
    def __init__(self, first_name,last_name,age,place_of_birth):
        User.__init__(self, first_name,last_name,age,place_of_birth)
        self.privileges = []
        

        self.privileges = Privileges()




class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        for p in self.privileges:
            print(f"Admin : {p}")



        
u1 = User('Nela' , 'Genina' , 17 , 'Ua')
u1.describe_user()
u1.greeting_user()

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()

u1.reset_login_attempts()
u1.increment_login_attempts()
u1.reset_login_attempts()



priv = Admin('Anelia' , 'Genina' , 17 , 'Ua')
priv.privileges.privileges = [' разрешено доб. сооб.',' раз. банить',' раз. удалять пользователя']
priv.privileges.show_privileges()
