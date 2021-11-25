def den():
  for p , i in students.items():
      print('-'*30)
      print(f"{p} решил :")
      for task in i :
          print(f"- {task}")

students = {
'Kiril':['task1','task2','task3','task4','task5','task6','task7','task8','task9','task10'],
'Renat':['task1','task2','task3'],
'Vania':['task1'],
'Yaroslav':['task1','task2','task3','task4','task5']
    }
den()
