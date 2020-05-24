#modify so each person can have more thna one favorite number. solution -> list in dictionary
favorite_num = {'bob': [43,2,4],
            'janis': [23,34,3],
            'fagis': [43,],
            'lamnda': [5,4,34],
                }

for names, numbers in favorite_num.items():
    print("\n" + names + " " + str(numbers))
    #had to run a nested for loop to print numbers without bracket 
    for num in numbers:
        print(num)
