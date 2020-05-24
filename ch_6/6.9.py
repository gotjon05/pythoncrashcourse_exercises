favorite_places = {
    'bob': {
        'favorite places': 'Grand Canyon',
        },
    'sara': {
        'favorite places': 'NYC',
        },
    'jansen':{
        'favorite places': 'las vegas',
        },
    }

#
for people, places in favorite_places.items():
    print(people + " " + places['favorite places'])

