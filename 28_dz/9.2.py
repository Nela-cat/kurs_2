class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()} and this restaurant have {self.cuisine_type} products")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")
 
restaurant = Restaurant('Felichita', 'fresh')
restaurant.describe_restaurant()

restaurant2 = Restaurant('Mac', 'fast_food')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Lena', 'italian')
restaurant3.describe_restaurant()

