class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()} , {self.cuisine_type} products")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")

class IceCreamStand(Restaurant):
     def __init__(self,restaurant_name,cuisine_type):
         Restaurant.__init__(self,restaurant_name,cuisine_type)       
         self.flavors = []



     def show_flavors(self):
        for f in self.flavors:
            print(f"ice cream : {f}")         
    
 


