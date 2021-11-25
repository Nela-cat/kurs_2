favorite_numbers ={
    'Nela' :{
        'first_favorite_number' : 13 ,
        'second_favorite_number' : 15 ,
        'third_favorite_number' : 136 ,
        
        
        }  ,
    
    'Dana' : {'first_favorite_number' : 11 ,
        'second_favorite_number' : 133 ,
        'third_favorite_number' : 156 ,
        } ,
    
    'Tom'  : {'first_favorite_number' : 3 ,
        'second_favorite_number' : 5 ,
        'third_favorite_number' : 16 ,
        } ,
    
    'Ben'  : {'first_favorite_number' : 90 ,
        'second_favorite_number' : 61 ,
        'third_favorite_number' : 1 ,
        } ,
    
    'Rer'  : {'first_favorite_number' : 89 ,
        'second_favorite_number' : 1 ,
        'third_favorite_number' : 36 ,
        } ,
    
    }
for i , p in favorite_numbers.items() :
    print('-' *40 ,'*')
    print(f"Человек под именем : {i} любит числа  {p['first_favorite_number']} {p['second_favorite_number']} {p['third_favorite_number']} ")
    print('-' *40 ,'*')
