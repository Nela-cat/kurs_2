players={
    'user_0':{
        'first_name':'Nela',
        'last_name':'Genina',
        'age':16,
        'country':'UK'}
    
    }
for p, i in players.items():
    print("-" *50 ,'*')
    print(f"Человек под именем {p}: ")
    players_info=f"{i['first_name']} {i['last_name']}"
    age=f" {i['age']}"
    country=f"Он проживает в стране: {i['country']}"
    print(f"\tИмя фамилия игрока: {players_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tСтрана: {country}")
    print("-" *50 ,'*')
