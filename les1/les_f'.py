Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mashon= ['bmw' , 'suzu' , 'mazda']
>>> print(mashon)
['bmw', 'suzu', 'mazda']
>>> message = f"я хочу зас марку мвшины"{mashon[1].title()}
SyntaxError: invalid syntax
>>> message = f"я хочу зас марку мвшины{mashon[1].title()}"
>>> print(message)
я хочу зас марку мвшиныSuzu
>>> 
>>>  mashin= ['bmw' , 'suzu' , 'mazda']
 
SyntaxError: unexpected indent
>>> mashin= ['bmw' , 'suzu' , 'mazda']
>>> print(mashin)
['bmw', 'suzu', 'mazda']
>>> message = f"я хочу зас марку мвшины{mashin[1].title()}"
>>> print(message)
я хочу зас марку мвшиныSuzu
>>>
mashin= ['bmw' , 'suzu' , 'mazda']
print(mashin)
del_item=mashin.pop()
print(mashin)
