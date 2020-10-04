class User():
    def __init__(self, first_name, last_name, email, phone_number):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.phone_number = phone_number
    

    def welcome_user(self):
        print("Welcome " + self.first.title() + " " + self.last.title())
    
    def describe_user(self):
        print("Our records show that your email address is " + self.email.title() + " and your phone number is " + str(self.phone_number)) 
bob = User("Bob", "jenkins", "borsch@aol.com", 232-324-2343)
victor = User("Victor", "frost", "frost@gmail.com", 734-323-3243)


bob.welcome_user()
bob.describe_user()

victor.welcome_user()
victor.describe_user()
    
