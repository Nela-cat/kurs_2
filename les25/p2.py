class Circle :
    PI = 3.14
    Circle_v =0
    
    def __init__(self,r):
        self.r = r
        Circle.Circle_v += 1
        
    def len_Circle(self):
        print(f" l ={2*self.PI*self.r}")
       
        
    def square(self):
        print(f" S= {self.PI*self.r**2}")



a=int(input("введите r"))
c1=Circle(a)
c1.len_Circle()
print(Circle.Circle_v)
c2=Circle(a)
c2.square()


print(Circle.Circle_v)
