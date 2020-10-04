

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")    


#instance 1
restaurant = Restaurant("cat", "dog")


#accessing attributes of an instance
print("i love " + restaurant.restaurant_name.title())
restaurant.cuisine_type

#calling methods defined in Restaurant Class
restaurant.describe_restaurant()
restaurant.open_restaurant()
