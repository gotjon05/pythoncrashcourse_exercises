class User():
    def __init__(self, first_name, last_name, email, phone_number):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0

    def welcome_user(self):
        print("Welcome " + self.first.title() + " " + self.last.title())

    def describe_user(self):
        print("Our records show that your email address is " + self.email.title() + " and your phone number is " + str(self.phone_number))

    def increment_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts + 1
        print("you have " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("there have been " + str(self.login_attempts))




bob = User("Bob", "jenkins", "borsch@aol.com", 232-324-2343)
victor = User("Victor", "frost", "frost@gmail.com", 734-323-3243)
new_user = User("bob", "jingles", "blah@aol.com", 212-343-2323)


new_user.increment_login_attempts(2)
new_user.increment_login_attempts(2)
new_user.increment_login_attempts(2)
new_user.reset_login_attempts()
new_user.increment_login_attempts(2)

bob.welcome_user()
bob.describe_user()
victor.welcome_user()
victor.describe_user()
