glos = {
    'remove()' : 'Метод удаляет первый соответствующий элемент ',
    'insert()':'метод вставляет элемент в список по указанному индексу ',
    'pop()':'метод удаляет с заданным методом из списка ',
    'del':'слово удаляет обьекты ',
    'f""':'строка берет значение переменных которое есть , и подставляет из в сторку',

    }

glos['.index()']= 'используется для вывода индекса элемента.' ,
glos['.count()']='используется для подсчета количества элементов в кортеже.',
glos['sum()']='складывает все элементы кортежа.',
glos['min()']='показывает элемент кортежа с наименьшим значением.',
glos['max()']='показывает элемент кортежа с максимальным значением.'

for g, z in glos.items():
    print('-' *40 ,'*')
    print(f"\n{g} : {z} ")
    
