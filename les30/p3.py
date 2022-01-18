class Shop :
    def __init__(self,shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
        
    def describe_shop(self):
        print(f"Shop name : {self.shop_name } , type : {self.store_type} , number of units: {self.number_of_units}")
    def open_shop(self):
        print(f'онлайн магазин {self.shop_name } відкритий')
        
stor= Shop('Ekea' , 'mas_marcet' )
stor.number_of_units=234


print(stor.shop_name)
print(stor.store_type)

stor.describe_shop()
stor.open_shop()

s = Shop('ATB' , 'mas_marcet '  )
stor.number_of_units=12314
s.describe_shop()
