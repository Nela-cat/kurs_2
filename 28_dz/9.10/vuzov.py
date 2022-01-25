from restoran import *
restaurant = Restaurant('Argone', 'boiled')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


ice = IceCreamStand('Argone','ice cream')
ice.flavors = ['vanilla','strawberry']


ice.show_flavors()
