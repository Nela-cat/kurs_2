name_users = {"Ivan": 15, "Denis": 24, "Renat": 15, "Kirill": 49, "Nela": 18}
user_auto = {"Zhigul": 1990, "Ferrari": 2021, "Volkswagen": 2020}
about_life = [name_users, user_auto]
print(about_life)
for i in about_life:
    print(i)

empty = []
for x in range(30):
    new_item = {"Color": "grey", "Speed": 50, "Temprature": -10}
    empty.append(new_item)
    print(empty)
for y in empty[:5]:
    print(y)
