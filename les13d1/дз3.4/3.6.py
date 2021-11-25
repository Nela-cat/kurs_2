persons = ['Nela','Dana','Anna']

for p in persons:
    print( f" хочу пригласить : {p}")

a = persons.pop(0)
print(f"извините {a} не сможет  прийти")

for p in persons:
    print(f" хочу пригласить : {p}")

print('мы купили большой стол ')

persons.insert(0,'Tom')

persons.insert(2,'lula')

persons.append('Ben')

for p in persons:
    print(f" хочу пригласить : {p}")
