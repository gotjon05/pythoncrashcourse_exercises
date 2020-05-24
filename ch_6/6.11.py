#dictionary called cities; create a dictionary of each city --> dictionary in a dictionary

cities = {
        'Atlanta': {
            'country':'USA',
            'population':'10000',
            'fact': 'bloop',
            },
        'NYC':{
            'country':'USA',
            'population':'10000',
            'fact': 'bloop',
            },
        'Boston':{
            'country':'USA',
            'population':'10000',
            'fact': 'bloop',
            }
        }

for city, city_info in cities.items():
    print(city + " " + str(city_info))
    print(city_info['country'])
