def month(n):
    for p, i in season.items():
        if n in p :
            print(i)
        else:
            print('Нету такого месяца')
            break    
        
season = {
(12,1,2):'winter',
(3,4,5):'spring',
(6,7,8):'sammer',
(9,10,11):'autumn',
    }   
nuber=int(input('введите номер месяца : '))
print(month(nuber))
