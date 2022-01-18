class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    def plo(self):
        print(f"S : {self.b*self.a}")
s=Rectangle(2,6)
s.plo()
