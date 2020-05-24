pizza = ['cheese', 'peperoni', 'mushroom', 'margarita', 'meatball', 'anchovi']
print(pizza[:3])


friend_pizza = pizza[:]

pizza.append('chicken')
friend_pizza.append('Broocoli')

for za in pizza:
    print("My favorite Pizza is " + za)

for pi in friend_pizza:
    print("My Friends favorite Pizza's are " + pi)

bad_pizza = friend_pizza.pop()

print("we dont like " + bad_pizza + " Pizza")


for pi in friend_pizza:
    print("My Friends favorite Pizza's are " + pi)

