
#-- dict of prices
menu = {
    "Popcorn": 50,
    "Soda": 30,
    "Sour candy": 30,
    "Sweet candy": 30,
    "Chocolate":40,
}

# items you will buy
cart = []

#  print menu
print("Hello! Welcome to the theater store.\n")
for item, price in menu.items():
    print(f"\n - {item}:{price}kr")


# while true
print("\nIf you want to buy something write it down below, else write 'q' to exit.")

while True:
    order = input("\nInput: ").lower()

    if order == "q":
        break

    if order in menu:
        cart.append(order)
        print(f"\n{order} added to cart. You now have {cart} in your cart.")
    else:
        print("\nSorry, we do not have that item.")



# receipt. takes the price of the items you had in the cart and combines it into a total price.

print ("\n\n-----RECEIPT-----")

total_price = 0

for item in cart:
    price = menu[item]
    total_price += price
    print(f"\n - {item}:{price}kr")


print(f"\nTotal: {total_price}kr", "\nThank you for your purchase.")



