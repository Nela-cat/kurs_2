gests= ['Tom' , 'Ben' , 'Alex', 'Ray']
print('Gests : ' , gests)
print(f"приглашается {gests[0]}")
print(f'приглашается {gests[1]}')
print(f'приглашается {gests[2]}')
print(f'приглашается {gests[3]}')

message = f"{gests[0]} не сможет прийти"
print(message)


gests[0] = 'Nela'
print('Gests : ' ,gests)

print(f"приглашается {gests[0]}")
print(f'приглашается {gests[1]}')
print(f'приглашается {gests[2]}')
print(f'приглашается {gests[3]}')


print ('У нас теперь больше мест и гостей соответственно ')
gests.insert(0 , 'Dana')
gests.insert(3 , 'Anna')
gests.append('Piter')
print('Gests : ' , gests)

print(f"приглашается {gests[0]}")
print(f'приглашается {gests[1]}')
print(f'приглашается {gests[2]}')
print(f'приглашается {gests[3]}')
print(f"приглашается {gests[4]}")
print(f'приглашается {gests[5]}')
print(f'приглашается {gests[6]}')

print ('тол не приедет так что сокращаем гостей ')

dell1= gests.pop(0)
print('Простите , я безумно сожалею ', dell1)

dell2= gests.pop(0)
print('Простите , я безумно сожалею ', dell2)

dell3= gests.pop(2)
print('Простите , я безумно сожалею ', dell3)

dell4= gests.pop(3)
print('Простите , я безумно сожалею ', dell4)

dell5= gests.pop(-1)
print('Простите , я безумно сожалею ', dell5)

print('Gests : ' ,gests)
print(f"Все в силе {gests[0]}")
print(f'Все в силе {gests[1]}')

del gests[0:2]
print(gests)
