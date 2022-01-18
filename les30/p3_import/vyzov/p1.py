from p_01 import *

stor= Shop('Ekea' , 'mas_marcet' )
stor.number_of_units=234


print(stor.shop_name)
print(stor.store_type)

stor.describe_shop()
stor.open_shop()

#a=int(input('введите ол. тов.   '))
#stor.set_number_of_units()

#stor.increment_number_of_units()



s = Shop('ATB' , 'mas_marcet '  )
stor.number_of_units=12314
s.describe_shop()


store_discount= Discount('Ekea' , 'mas_marcet' )
store_discount.discount_products=['сыр','молоко','чай']
store_discount.get_disconts_products()
