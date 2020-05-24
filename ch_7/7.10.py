places = []
prompt = "Where would you go for vacation"

active = True
while active == True:
    dream_vacation = input(prompt)
    if dream_vacation == 'quit':
        break
    else:
        places.append(dream_vacation)

for place in places:
    print(place)

