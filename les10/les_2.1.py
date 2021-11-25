def Pechat():
    while arr_models:
        title1 = arr_models.pop(0)
        arr_python.append(title1)
        print(arr_python)
def Print (arr_python):
    for text in arr_python:
        print(f'обьект {text} - напечатался')
        
arr_models = ['чехол','пенал','ручка','кирпич']
arr_python = []
Pechat(arr_models,arr_python)
Print(arr_python)
