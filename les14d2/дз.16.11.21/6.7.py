people={
    'user_0':{
        'first_name':'nela',
        'last_name':'Genina',
        'age':16,
        'country':'UK'},
    'user_1':{
        'first_name':'Vania',
        'last_name':'Tsurkan',
        'age':15,
        'country':'Ukraine'}
    }
for p, i in people.items():
    print("❤"*27)
    print(f"Человек по имени {p}: ")
    players_info=f"{i['first_name']} {i['last_name']}"
    age=f"Ему {i['age']}"
    country=f"Он проживает в стране: {i['country']}"
    print(f"\tИмя фамилия человека: {players_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tСтрана: {country}")
