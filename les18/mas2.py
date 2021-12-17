#import random
#n = int(input('1')) #h
#m =int(input('2')) #l

#a =[[random.randint(0,3)for g in range(m)] for i in range(n)]


#print('-'*20)
#for i in a :
   #print(f'|{i}|')
#print('-'*20) 


#h = [a[i][g] for  i in range(n) for g in range(m) if i == g ]
#print(h)


import random
pu = int(input('1'))
pa = int(input('2'))
gg = [[random.randint(0,9) for rer in range(pu)] for nin in range(pa)]
for i in gg :
    print(i)
print('-'*20)   
strw=[gg[rer][nin] for nin in range(pu) for rer in range(pa) if rer==nin]
print(strw)
