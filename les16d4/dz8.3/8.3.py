def make_shirt(size,*nazvanie):
    
    print(f"Вы выбрали футболку с таким текстом {tekst} и с размером {size.title()}:")
    
razmer = str(input('Введите размер футболки:'))
tekst = str(input('Введите текст на футболке:'))
make_shirt(razmer, tekst)
