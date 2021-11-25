models = ['auto','ruchka','iphone','xiaome','huawei']
ready_models = []
def alwswnncry(a, b):
    while models:
        awk = a.pop()
        b.append(awk)
        print(b)
def alwswnnsrt(b):
    for i in b:
        print(f"Напечеталась модель {i.title()}")
alwswnncry(models, ready_models)
alwswnnsrt(ready_models)
