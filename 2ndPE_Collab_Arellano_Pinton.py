menu = {
    1: ("Burger", 50),
    2: ("Fries", 35),
    3: ("Soft Drink", 25),
}


def get_order():
    order = []

    print("MENU")
    for number, (name, price) in menu.items():
        print(f"{number}. {name} - ₱{price:.2f}")

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
        print(f"Added: {qty} x {name}")

        while True:
            more = input("Order another product? (y/n): ").lower()
            if more in ("y", "n"):
                break
            print("Type y or n.")

        if more == "n":
            break

    return order


def print_receipt(order):
    total = 0

    print()
    print("=" * 40)
    print("Friend and Fries".center(40))
    print("=" * 40)
    print(f"{'Item':<14}{'Qty':<6}{'Price':<10}{'Subtotal'}")
    print("-" * 40)

    for item in order:
        print(f"{item['name']:<14}{item['qty']:<6}{item['price']:<10.2f}{item['subtotal']:.2f}")
        total += item["subtotal"]

    print("-" * 40)
    print(f"TOTAL: ₱{total:.2f}")
    print("=" * 40)


order = get_order()
print_receipt(order)
