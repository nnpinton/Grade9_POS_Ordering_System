menu = {
    1: ("Burger", 50.00),
    2: ("Fries", 35.00),
    3: ("Soft Drink", 25.00),
}


def get_order():
    order = []

    print("MENU")
    for number, (name, price) in menu.items():
        print(number, name, "PHP", price)

    while True:
        while True:
            try:
                choice = int(input("Select a product number: "))
                if choice in menu:
                    break
                print("That number is not on the menu.")
            except ValueError:
                print("Enter a number.")

        while True:
            try:
                qty = int(input("Quantity: "))
                if qty > 0:
                    break
                print("Quantity must be at least 1.")
            except ValueError:
                print("Enter a number.")

        name, price = menu[choice]
        subtotal = price * qty
        order.append({"name": name, "price": price, "qty": qty, "subtotal": subtotal})
        print("Added:", qty, "x", name)

        while True:
            more = input("Order another product? (y/n): ").lower()
            if more in ("y", "n"):
                break
            print("Type y or n.")

        if more == "n":
            break

    return order


if __name__ == "__main__":
    print(get_order())