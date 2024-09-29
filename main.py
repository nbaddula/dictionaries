import menu as data
import functions

def show_main_menu():
    menu = data.create_menu()  # Create the menu at the start
    
    while True:
        print("\nWelcome to Nainika's Diner!")
        role = input("Are you a (C)ustomer or a (M)anager? (Q to quit): ").strip().upper()
        
        if role == 'C':  # Customer actions
            handle_customer(menu)
        elif role == 'M':  # Manager actions
            handle_manager(menu)
        elif role == 'Q':
            break
        else:
            print("Invalid choice. Please enter C for Customer, M for Manager, or Q to quit.")
            
def handle_customer(menu):
    current_order = []
    while True:
        print("\nCustomer Menu")
        print("N for a new order")
        print('X for close orders and print the check')
        print('R to reset the order')
        print('Q for quit to main menu')
        user_choice = input('Your input: ').strip().upper()
        
        if user_choice == 'Q':
            break
        elif user_choice == 'N':
            print('New order')
            while input('Add a dish? (y/n): ').strip().lower() == 'y':
                item_code, quantity = input("Enter item code and quantity (e.g., E1 2): ").split()
                if functions.process_customer_request(menu, item_code, quantity):
                    current_order.append((item_code, int(quantity)))
                print('Your order: ', current_order)
        elif user_choice == 'X':
            print('Closing orders and printing the check')
            print_check(current_order, menu)
        elif user_choice == 'R':
            current_order = []  # Reset the order
        else:
            print("Invalid choice. Please enter N for new order, X for close and print check, R to reset, or Q to quit.")

def handle_manager(menu):
    while True:
        print("\nManager Menu")
        print("U to update the menu (change price, description, or both)")
        print('A to add a menu item')
        print('R to remove a menu item')
        print('D to display the menu')
        print('Q to quit to main menu')
        user_choice = input('Your input: ').strip().upper()
        
        if user_choice == 'Q':
            break
        elif user_choice == 'U':
            update_menu_item(menu)
        elif user_choice == 'A':
            add_menu_item(menu)
        elif user_choice == 'R':
            remove_menu_item(menu)
        elif user_choice == 'D':
            functions.display_menu(menu)
        else:
            print("Invalid choice. Please enter U to update, A to add, R to remove, D to display, or Q to quit.")

def print_check(current_order, menu):
    print("\nYour order:")
    total = 0
    for item_code, quantity in current_order:
        for item in menu:
            if item['code'] == item_code:
                print(f"{item['name']} (x{quantity}): ${item['price'] * quantity}")
                total += item['price'] * quantity
    print(f"\nTotal: ${total}")
    print(f"Taxes (10%): ${total * 0.10}")
    print(f"Grand Total: ${total * 1.10}")

def update_menu_item(menu):
    code = input("Enter the item code to update: ")
    
    # Ask the manager what they want to update
    update_choice = input("Would you like to update (N)ame, (P)rice, or (B)oth? ").strip().upper()

    new_name = None
    new_price = None
    
    if update_choice == 'N':
        new_name = input("Enter the new name: ")
    elif update_choice == 'P':
        new_price = int(input("Enter the new price: "))
    elif update_choice == 'B':
        new_name = input("Enter the new name: ")
        new_price = int(input("Enter the new price: "))

    functions.update_menu(menu, code, new_name, new_price)

def add_menu_item(menu):
    code = input("Enter the new item code: ")
    name = input("Enter the new item name: ")
    price = int(input("Enter the item price: "))
    stock = int(input("Enter the item stock: "))
    functions.add_item(menu, code, name, price, stock)

def remove_menu_item(menu):
    code = input("Enter the item code to remove: ")
    functions.remove_item(menu, code)

if __name__ == "__main__":
    show_main_menu()