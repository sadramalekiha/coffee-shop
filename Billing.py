from Order import orders

def calculate_discount(total):
    if total > 1_000_000:
        return total * 10 // 100
    return 0

def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total

def print_invoice():
    if not orders:
        print("Please place an order before requesting an invoice.\n")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("\n============== Cafe Invoice ==============")
    for order in orders:
        subtotal = order["price"] * order["quantity"]
        print(
            f"{order['product']} | "
            f"Quantity: {order['quantity']} | "
            f"Amount: {subtotal:,} Toman"
        )

    print("------------------------------------------")
    print(f"Order total:       {total:,} Toman")
    print(f"Discount:          {discount:,} Toman")
    print(f"Amount to pay:     {final_amount:,} Toman")
    print("==========================================\n")
