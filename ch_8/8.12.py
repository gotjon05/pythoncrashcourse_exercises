#user provides input that gets passed to function. function 
sandwich_list = ["paneer", "cheese", "mayo", "mushrooms"]




def sandwich(*ingredients):
    for item in ingredients:
        print(item)



sandwich(sandwich_list)
sandwich("bacon", "lettuce", "tomato")

