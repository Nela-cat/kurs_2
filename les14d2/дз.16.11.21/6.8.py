pets={
    'Lulu':{
        'kind_of_animal':'dog',
        'pet_owner_name':'nela',
        },
    'Jorj':{
        'kind_of_animal':'cat',
        'pet_owner_name':'Ela',
        
        }
    }
for p, i in pets.items():
    print("❤"*27)
    print(f"животное по имени {p}: ")
    kind_of_animal = f'Вид животного  {i["kind_of_animal"]}'
    pet_owner_name = f'хозяин по имени   {i["pet_owner_name"]}'
    print(kind_of_animal)
    print(pet_owner_name)
    
