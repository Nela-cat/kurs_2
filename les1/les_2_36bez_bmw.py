

mashin= ['bmw' , 'suzu' , 'mazda']
print(mashin)
message = f"я не хочу эту марку мвшины {mashin[0].title()} давайте без нее"
print(message)
del_item=mashin.pop(0)
print(mashin)
a =int (input('a='))
if a>12:
    print('a>12')
elif a <12:
    print('a<12')
else:
    print('non')
