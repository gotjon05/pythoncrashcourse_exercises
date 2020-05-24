class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + " " + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


#instances
bob = User('glob', 'Burger')
bob.describe_user()
bob.greet_user()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
#made the mistake by doing bob.login_attempts(), with the error int object is not callable 
print("  Login attempts: " + str(bob.login_attempts))
bob.reset_login_attempts()
print("  Login attempts: " + str(bob.login_attempts))





jar = User('lard', 'buttocks')



