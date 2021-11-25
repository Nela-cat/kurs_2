persons = ['Nela','Dana','Anna']
for p in persons:
    print( f" хочу пригласить : {p}")
    
print(f"всего приглашено {len(persons)} гостя")

print('прийти в таком порядке')

print(sorted(persons , reverse=True))


persons.insert(0,'Tom')

persons.append('Ben')

for p in persons:
    print(f"у нас пополнение {p}")

print('прийти в таком порядке')

print(sorted(persons , reverse=False))

