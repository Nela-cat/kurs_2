
#import cod_fun ///1
#print('введи ''stop'' если хочешь прекратить')

#while True:
    
    #vop_1 = str(input('Введите  имя исполнителя:'))
    #if vop_1 == 'stop':
            #break
    #vop_2 = str(input('Введите один из  его альбомов : '))
    #if vop_2 == 'stop':
            #break
    #rez = cod_fun.make_album(vop_1,vop_2)
    #print(rez)



#from cod_fun import make_album   ///2
#print('введи ''stop'' если хочешь прекратить')

#while True:
    
    #vop_1 = str(input('Введите  имя исполнителя:'))
    #if vop_1 == 'stop':
            #break
    #vop_2 = str(input('Введите один из  его альбомов : '))
    #if vop_2 == 'stop':
            #break
    #rez = make_album(vop_1,vop_2)
    #print(rez)




#from cod_fun import make_album as make ///3
#print('введи ''stop'' если хочешь прекратить')

#while True:
    
    #vop_1 = str(input('Введите  имя исполнителя:'))
    #if vop_1 == 'stop':
            #break
    #vop_2 = str(input('Введите один из  его альбомов : '))
    #if vop_2 == 'stop':
            #break
    #rez = make(vop_1,vop_2)
    #print(rez)



#import cod_fun as make 
#print('введи ''stop'' если хочешь прекратить')

#while True:
    
    #vop_1 = str(input('Введите  имя исполнителя:'))
    #if vop_1 == 'stop':
            #break
    #vop_2 = str(input('Введите один из  его альбомов : '))
    #if vop_2 == 'stop':
           # break
    #rez = make.make_album(vop_1,vop_2)
    #print(rez)


from cod_fun import *
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
