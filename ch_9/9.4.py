
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("The number of customers served is currenty " + str(self.number_served))

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print("The number of customers served is currenty " + str(self.number_served))


#instance 1
catdog_restaurant = Restaurant("cat", "dog")
#new instance
restaurant = Restaurant("burts", "french")

#accessing attributes of an instance
print("i love " + restaurant.restaurant_name.title())
catdog_restaurant.cuisine_type
print("we have served " + str(restaurant.number_served))

#calling methods defined in Restaurant Class
catdog_restaurant.describe_restaurant()
catdog_restaurant.open_restaurant()
restaurant.set_number_served(999)
restaurant.increment_number_served(1)
