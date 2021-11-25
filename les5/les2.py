def pizza (*nazvanie):
    print(f"вы выбрали такую такую пиццу ===> {nazvanie}")
    for i in nazvanie:
        print(f'-{i.title()}')
    
pizza('gavai')
pizza('peperoni' , '4sira', 'masna')
