

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
invited_people = ['bob', 'rob', 'todd', 'god', 'edward', 'joshua', 'lorde', 'jen']

for people in favorite_languages.keys():
    if people in invited_people:
        print("thank you for taking the poll " + people)
    else:
        print("please take our poll " + people)


