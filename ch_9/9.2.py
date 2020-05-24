class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):

        #attributes
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type

        #method
    def describe_restaurant(self):
        print("the restaurant is called " + self.restaurant_name.title() + "and serves " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is open")

#instance 
taco_bell = Restaurant('taco bell', 'Fast Food')
taco_bell.restaurant_name
taco_bell.cuisine_type

mcdonalds = Restaurant('Mcdonalds', 'Fast Food')
mcdonalds.describe_restaurant()

china_palace = Restaurant('china Palace', 'Chinease Food')
china_palace.describe_restaurant()


#call methods for each attributres individualy
print(china_palace.restaurant_name.title())
print(taco_bell.restaurant_name.title())
print(taco_bell.cuisine_type.title())

#call method:give name of instance and method you want to call
taco_bell.describe_restaurant()
taco_bell.open_restaurant()

