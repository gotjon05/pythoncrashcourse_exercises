#super/parent class
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

#does not inherit from any other class
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    #method moved from electriccar class to battery class
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        


#when creating child class, parent must be part of the file
#name of parent class in parenthesis 
class ElectricCar(Car):
    """Represent aspects of a car, specific to electrical vehicles """
    #takes the info required to make a car instance
    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        #super creates connection between parent and child calss
        #tells python to call the __init__ method from electriccar which an electric car instance all attributes of the parent class
        super().__init__(make, model, year)
        #attributes for child class
        #tells python to create a new instance of Battery and store instance in self.battery_size
        self.battery_size = 70
        #tells python to create a new instance of battery and store that instance in attribute self.battery. any electric car instance will now have a bettery instance created automaticly 
        self.battery = Battery()
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


    
    #def describe_battery(self):
     #   """print statement describing batter size """
      #  print("This car has a " + str(self.battery_size) + "-kwh battery")



#instance of electriccar class and stored in my_telsa
#Class the __init__ method defined by ElectricCar which in turn tells python to call __init__ method defined in parent class car
my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.get_range()











