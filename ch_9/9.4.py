class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):

        #attributes
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0

        #method
    def describe_restaurant(self):
        print("the restaurant is called" + self.restaurant_name.title() + "and serves " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is open")

    #modify attribute value through method
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

    
#instance 
taco_bell = Restaurant('taco bell', 'Fast Food')
taco_bell.restaurant_name
taco_bell.cuisine_type


restaurant = Restaurant('Bobs Burgers', 'Burgers')

restaurant.number_served = 430
print(restaurant.set_number_served(40))
print("after today the restaurant will have served " + str(restaurant.increment_number_served(342)))


print(taco_bell.restaurant_name.title())
print(taco_bell.cuisine_type.title())

#call method:give name of instance and method you want to call
taco_bell.describe_restaurant()
taco_bell.open_restaurant()


