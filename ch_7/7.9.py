sandwich_orders = ['Pastrami', 'BLT', 'Pastrami', 'Pastrami', 'Grilled Cheese Sandwich', 'Pastrami', 'Tuna Melt']
finished_sandwich = []

print("\nthe deli has run out of pastrami")

#made a mistake: while sandwich_orders == true: (nothing printed because condition was not met)
while sandwich_orders:
    if 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
    else:
        finished = sandwich_orders.pop()
        print("Serving " + finished)
        finished_sandwich.append(finished)


for finished in finished_sandwich:
    print(finished.title())
