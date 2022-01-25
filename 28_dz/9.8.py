class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        for p in self.privileges:
            print(f"Admin : {p}")

admin=Privileges()        
admin.privileges = [' зрешено доб. сооб.',' раз. банить',' раз. удалять пользователя']
admin.show_privileges()            
