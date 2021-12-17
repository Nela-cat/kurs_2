a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new=[items if items<5 else "False" for items in a]
print(new)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new=[items if items<5 else "False" for items in a]
print(new)


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
for i in numbers:
    if i%2==0:
        print(i)
    elif i==237:break


age=int(input("1= "))
if age<2:
    print("Mладениц")
elif age>=2 and age<4:
    print("Мфлыш")
elif age>=4 and age<13:
    print("реб")
elif age>=13 and age<20:
    print("подр.")
elif age>=20 and age<65:
    print("взрослый")
elif age>=65:
    print("пож.")


b = []
while True:
    vop_1 = str(input('Введите  имя :'))
    
    if vop_1 == 'stop':
            break
    else:
        b.append( vop_1)
print(f"Поздравляю, Вы зарегестрированы, {b}")




i= ['pizza', 'falafel', 'carrot cake']

d=[ m for m in i]
s = str(input('eda'))
d.append(s)
print(i)
print(d)





lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
a=[]
sum=0
for i in lst:
    if i<=30 and i%3==0:
       a.append(i)
    else:
        sum+=i
print(f" чис. с усл. :{a}")
print(sum)





diction = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
for i in diction.values():
    if i>=2:
        print(i)




keys = ["a", "b", "c", "d", "e", "g"]
values = [1,2,3,4,5,6]
c = {i:g for i, g in zip(keys, values)}
print(c)
for i,g in c.items():
    print(f"я знаю твой ключ {i} его значение  {g}")



g = {"Bali": 221, "London":567, "Deli": 345}
del g['Bali']
del g['London']
print(g)




dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
c = {i:"event" if dic[i]%2==0 else "odd" for i,g in dic.items()}
print(c)




import random
n=int(input("1= "))
m=int(input("1= "))
t=int(input("stol= "))
r=int(input("stol= "))
matrica = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for f in matrica:
    print(f)
diagonal = [matrica[r][t] for r in range(n) for t in range(m) if r == t]
print(f" Diagonal :{diagonal}")
stolbec = [matrica[t-1][w] for w in range(n)]
print(f" stroka :{stolbec}")
