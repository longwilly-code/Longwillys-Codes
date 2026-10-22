
#-- dict of prices
menu = {
    "popcorn": 50,
    "soda": 30,
    "sour candy": 30,
    "sweet candy": 30,
    "chocolate":40,
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
    order = input("\nInput: ").lower().strip()

    if order == "q":
        break


    if order in menu:
        cart.append(order)
        print(f"\n{order} added to cart. You now have {', '.join(cart)} in your cart.")
    else:
        print("\nSorry, we do not have that item.")



# receipt. takes the price of the items you had in the cart and combines it into a total price.



total_price = 0
if not cart:
            print("Have a nice day!")
else:
    print ("\n\n-----RECEIPT-----")
    for item in cart:
        price = menu[item]
        total_price += price
        print(f"\n - {item}:{price}kr")

    print(f"\nTotal: {total_price}kr", "\nThank you for your purchase.")



