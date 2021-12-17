a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print(i)


#2
import random
n=int(input("ved kol"))
numder=[random.randint(0,15)  for i in range(n)]
print(number)
p=1
for i in number:
    p*=i
print(f"rezultat : {p}")
print(number[0])
print(number[-1])


#3
lst=[386, 462, 47, 418, 907, 344, 236, 566, 597, 237, 217]
for i in lst:
    if i%2=0:
        print(i)
    elif i==237:
        break



#4
users=["user1", "user2", "user3", "user4"]
var=[]
while users:
    a=users.pop(0)
    print(f"pol {a} vare.")
    var.append(a)
print(var)




#6
a=["burger", "pizza", "sushi"]
b=a[:]  # срез
print(a)
print(b)
c=str(input("m :"))
b.append(c)
print(b)



#7
a=[11, 5, 8, 32, 3, 20 ,30, 132, 21, 129, 55, 9, 20]
for i in a:
    if i<30 and i%3==0:
    print(i)
    else:
    z+=i
print(z)




#8
a={"a":2, "b":4, "c":6, "d":8}
for i in v.values():
    if i>2:
    print(i)

dict={i:j for}


#9
dict={"a":1, "b":2, "c":3, "d":4}
x={i:"even" if dict[i]%2==0 else "odd" for i,j in dict.items()}

#10
import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
diagonal = [matrix[w][q] for w in range(n) for q in range(m) if w==q]
print('Главная диагональ ===>',diagonal)
k = int(input('Номер строки'))
p = int(input('Номер столбца'))
item = [matrix[k-1][w] for w in range(m)]
item1 = [matrix[q][p-1] for q in range(n)]
print(item)
print(item1)
r = int(input('Номер строки элемента'))
t = int(input('Номер столбца элемента'))
item2 = matrix[r-1][t-1]
print(item2)
