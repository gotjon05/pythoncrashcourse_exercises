class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(self.first_name + " " + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())


class Privileges():
    def __init__(self, privileges = []):
        self.privileges = privileges


    def show_privileges(self):
        for priv in self.privileges:
            print('-' + priv)



class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #self.privileges = []
        #Make a Privileges instance as an attribute in the Admin class
        #create a new instance of privileges with a default value of [] and store that in the attribute self.prvileges. This will happen everytime the __init__ method is called. 
        #any admin instance wil now have a privleges instance created automatically 
        self.privileges = Privileges()



    #moved to Privlages class
    #def show_privileges(self):
      #  for priv in self.privileges:
       #     print('-' + priv)


eric = Admin('eric', 'matthes')
eric.privileges.show_privileges()






#instances
bob = User('glob', 'Burger')
jacob = User("jacob", "larrs")
bacon = User("bacon", "butt")

print(bob.describe_user())

bob.describe_user()
bob.greet_user()


admin = Admin('Bob', 'Garfunkel')

#updates attribute
admin.privileges = ["can add post", "can delete post", "can ban user"]
admin.greet_user()
admin.describe_user()
admin.show_privileges()
