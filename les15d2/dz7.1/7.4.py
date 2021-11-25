prompt = "\nПривет! введи топпинг для пиццы "
prompt += "\nВведите “quit” для завершения заказа"
message = ""
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
        print('заказ  принят')
    else:
        print(message)
