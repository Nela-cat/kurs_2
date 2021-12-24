import math
x = int(input('x='))
e  = int(input('e='))
if x>=1:
    y = e**(-abs(x))
elif  abs(x)<1:
    y= math.log10(math.sqrt(1-x**2))
elif x<=-1:
    y  = (math.atan(x))

print('y=' ,y)
    
