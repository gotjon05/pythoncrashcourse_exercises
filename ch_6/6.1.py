person = {
        'first_name': 'bob', 
        'last_name': 'grunk', 
        'age': 43, 
        'city': 'Chicago'
        }

print(person['first_name'].title())



#items() retuns a liust of key-value pairs 
for key, value in person.items():
    print(key + ": " + str(value))
