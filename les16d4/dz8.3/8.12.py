def sandwish(*ing):
    print(f'ваш сэндвич состоит из : {ing} ')
    for i in ing:
            print(f"- {i.title()}")

a1 = str(input('ведите ингридиент номер 1'))
a2 = str(input('ведите ингридиент номер 2'))
a3 = str(input('ведите ингридиент номер 3'))

sandwish(a1 ,a2 ,a3)
