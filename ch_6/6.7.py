person_1 = {
        'first_name': 'bob', 
        'last_name': 'grunk', 
        'age': 43, 
        'city': 'Chicago'
        }

#print(person['first_name'].title())

#items() retuns a liust of key-value pairs 
#for key, value in person.items():
 #   print(key + ": " + str(value))

#make two dictionaries of different people, store all three dictionaires in a list called people

person_2 = {
    'first_name': 'bobby',
    'last_name': 'jorgan',
    'age': 23,
    'city': 'Chicago'
    }


person_3 = {
    'first_name': 'sally',
    'last_name': 'wether',
    'age': 43,
    'city': 'Chicago'
    }

people = [person_1, person_2, person_3]

for person in people:
    print(person)




