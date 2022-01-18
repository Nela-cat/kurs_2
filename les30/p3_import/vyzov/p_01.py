class Shop :
    def __init__(self,shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
         
    def describe_shop(self):
        print(f"Shop name : {self.shop_name } , type : {self.store_type} , number of units: {self.number_of_units}")
    def open_shop(self):
        print(f'онлайн магазин {self.shop_name } відкритий')


    def set_number_of_units(self):
        self.a=a
        print(f" кол тов {a}")

    #def increment_number_of_units(self) :
        #self.a += 1
        #print(f" new  кол тов {self.a}")



class Discount(Shop) :
    def __init__(self,shop_name,store_type):
        Shop.__init__(self,shop_name,store_type)
        self.discount_products=[]

    def get_disconts_products(self) :
        for p in self.discount_products:
            print(f"disconts products : {p} ")
