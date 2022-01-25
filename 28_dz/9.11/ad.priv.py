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
