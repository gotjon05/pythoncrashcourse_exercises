#function stores info abotu cars into dictionary 

"""def make_car(manufacturer, model_name, **misc):
    #Build a dictionary containing everything we know about car
    cars = {}
    cars['maker'] = manufacturer
    cars['model'] = model_name

    for key, value in misc:
        cars['key'] = value
    return cars
"""

def make_car(*args, **kwargs):
    car_info={}
    car_info["maker"] = args[0]
    car_info["model"] = args[1]

    for key, val in kwargs.items():
        car_info[key] = val
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
