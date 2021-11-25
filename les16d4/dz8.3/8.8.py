def make_album(name,album):
    
    print(f"Вы ввели сполнителя по имени :   {name.title()} и его альбом : {album.title()}")

print('введи ''stop'' если хочешь прекратить')

while True:
    
    vop_1 = str(input('Введите  имя исполнителя:'))
    if vop_1 == 'stop':
            break
    vop_2 = str(input('Введите один из  его альбомов : '))
    if vop_2 == 'stop':
            break
    rez = make_album(vop_1,vop_2)
    print(rez)
        
