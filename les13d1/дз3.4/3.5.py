persons = ['Nela','Dana','Anna']

for p in persons:
    print( f" хочу пригласить : {p}")

a = persons.pop(0)
print(f"извините {a} не сможет  прийти")

for p in persons:
    print(f" хочу пригласить : {p}")
