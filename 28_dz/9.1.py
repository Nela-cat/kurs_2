class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()} , {self.cuisine_type} products")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")
 
restaurant = Restaurant('Argone', 'boiled')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
