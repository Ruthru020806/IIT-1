menu = {"Parota": 12.00,"Chickenrice": 105.50,"Chickennoodles": 90.25,"Chicken65": 54.00,"Karidosa": 40.50,"Muttongravy":32.08}

def display_restaurant_system():
    print("\n--- WELCOME TO MADURAI MUNIYANDI VILLAS RESTAURANT---")
    print("Item".ljust(15) + "Price")
    print("-" * 25)
    for item, price in menu.items():
        print(f"{item.ljust(15)}${price:.2f}")

    total_bill = 0.0
    order_list = []

    while True:
        order = input("\nEnter your order (or type 'done' to finish): ").strip().capitalize()

        if order == 'Done':
            break
        if order not in menu:
            print("Invalid item. Please select from the menu above.")
        else:
            price = menu[order]
            total_bill += price
            order_list.append(order)
            print(f"Added {order} to your order. Current subtotal: ${total_bill:.2f}")
    if total_bill > 0:
        tax = total_bill * 0.05
        grand_total = total_bill + tax

        print("\n" + "="*30)
        print("FINAL RECEIPT")
        print("="*30)
        for item in set(order_list):
            print(f"{item} x{order_list.count(item)}")

        print(f"\nSubtotal: ${total_bill:.2f}")
        print(f"Tax (5%):  ${tax:.2f}")
        print(f"TOTAL:     ${grand_total:.2f}")
        print("="*30)
        print("Thank you Come again!")
    else:
        print("No items ordered. Goodbye!")

if __name__ == "__main__":