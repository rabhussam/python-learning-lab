menu = {"pizza": 2.00,
        "burger": 5.00,
        "soda": 1.00}
cart = []
total = 0

while True:
    order = input("What would you like to order (q to quit):").lower()
    if order == "q":
        break

    elif menu.get(order) is not None:
        total += menu.get(order) # ------ (.get) is basically get the VALUE of my key {key:value}
        cart.append(order) # ------ this just gives you the key same as you wrote it

print(f"${total:.2f}")
print(cart, end=" ")
