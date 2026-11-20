from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice


def main():
    while True:
        print("========== Coffee Shop ==========")
        print("1. Display cafe menu")
        print("2. Place an order")
        print("3. Display orders")
        
        print("4. Calculate total")
        print("5. Print invoice")
        print("6. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            total = calculate_total()
            print(f"Current order total: {total:,} Toman\n")
        elif choice == "5":
            print_invoice()
        elif choice == "6":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
