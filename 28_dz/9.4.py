class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()} , {self.cuisine_type} products")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")


    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,add):
        self.number_served += add
        print(f" новое кол. гостей : {self.number_served}")
 
restaurant = Restaurant('Argone', 'boiled')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number served:  {restaurant.number_served}")



restaurant.number_served = 600
print(f"Number served:  {restaurant.number_served}")



#restaurant.number_served = 300
#print( f"Number served:  {restaurant.number_served}")

add = int(input('ведите доп. гост.'))
restaurant.increment_number_served(add)







 


