menu = {
    "coffee": 80_000,
    "tea": 50_000,
    "cake": 120_000,
}


def show_menu():
    print("\n========== Cafe Menu ==========")
    for product, price in menu.items():
        print(f"{product:<10} : {price:,} Toman")
    print("===============================\n")
