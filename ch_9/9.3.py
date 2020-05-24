class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(self.first_name + " " + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

#instances
bob = User('glob', 'Burger')
jacob = User("jacob", "larrs")
bacon = User("bacon", "butt")

print(bob.describe_user())

bob.describe_user()
bob.greet_user()


