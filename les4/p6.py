import math
x = int(input('x='))
e = int(input('e='))
if abs(x)<2:
    y = x-e**x
elif x<=(-2):
    y =math.log10(x**2)
elif x>=2:
    y = math.sin(x)**2
print('y=' , y)    
