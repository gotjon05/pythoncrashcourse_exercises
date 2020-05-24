sandwich_orders = ['BLT', 'Grilled Cheese Sandwich', 'Pastrami Sandwich', 'Tuna Melt']
finished_sandwich = []

#made a mistake: while sandwich_orders == true: (nothing printed because condition was not met)
while sandwich_orders:
    finished = sandwich_orders.pop()
    print("Serving " + finished)
    finished_sandwich.append(finished)


for finished in finished_sandwich:
    print(finished.title())
