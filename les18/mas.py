n =3
m =6
a =[[2] *m for i in range(n)]
print(a)
print('-'*20)
for i in a :
    print(f'|{i}|')
print('-'*20) 



u =4 #l
l= 5 #h
j= [[5]*u for i in range(l)]
print('-'*20)
for i in j :
    print(f'|{i}|')
print('-'*20)

mw = 5
er =8
a = [["t"]*mw for i in range(er)]
print('-' * 17)
for i in a :
    print(f"|{i}|")
print('-' * 17)   


ds =5
da = 4
a = [['@']*ds for i in range(da)]
for i in a :
    print(i)

import random
st = int(input('1'))
re = int(input('2'))
te= [[random.randint(0,5) for i in range(re)] for g in range(st)]
for d in te :
    print(d)
rar=[te[i][g]for i in range(re) for g in range(st) if i==g]    
print(rar)
