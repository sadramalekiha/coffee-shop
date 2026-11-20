from Menu import menu

orders = []


def add_order():
    
    product = input("Enter a product name (coffee / tea / cake): ").strip().lower()

    if product not in menu:
        print("This product is not available on the menu. Please choose a listed product.\n")
        return

    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Quantity must be a whole number.\n")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.\n")
        return

    orders.append({
        "product": product,
        "price": menu[product],
        "quantity": quantity,
    })
    print(f"Your order for {quantity} {product}(s) has been placed successfully.\n")


def show_orders():
    if not orders:
        print("No orders have been placed yet.\n")
        return

    print("\n========== Current Orders ==========")
    for index, order in enumerate(orders, start=1):
        subtotal = order["price"] * order["quantity"]
        print(
            f"{index}. Product: {order['product']} | "
            f"Unit price: {order['price']:,} Toman | "
            f"Quantity: {order['quantity']} | "
            f"Subtotal: {subtotal:,} Toman"
        )
    print("====================================\n")
