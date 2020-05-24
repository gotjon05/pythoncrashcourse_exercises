
prompt = "please enter your age"
prompt += "please quit to exit"

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("no cost")
    elif age < 13:
        print("ticket is 10")
    else:
        print("you ticket is 15")
