foods = ["Apple", "Coconut", "Chocolate", "Burger", "Fries"]
price = [2, 5, 3, 7, 4]
total = 0
order = []
print(foods)
while True:
    food = input("What food would you like to order (Q to quit):")
    if food.lower() == "q":
        print("Thank you for ordering")
        break
    elif not food in foods:
        print("That's not on the menu try again!")
    elif food in foods:
        i = foods.index(food)
        cost = price[i]
        total += cost
        order.append(food)
        print(f"A {food} is ${cost}")
print("You ordered:", ", ".join(order))
print(f"Total: ${total}")




