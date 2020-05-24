
# a class is a set of instructions to create an instance
class Dog():
    def __init__(self,name,age):
        """ intialize name and age attributes """
        self.name = name
        self.age = age


    #methods (functions within class)
    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + "rolled over")


#instance that calls the init method which creates an instance representing particular name, age attributes
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")



#access attributes
#pythohn look sat instance my_dog and finds attributes name associated with my_dog
my_dog.name

#call method:give name of instance and method you want to call
my_dog.sit()
my_dog.roll_over()



