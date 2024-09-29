import random

menu_items = [
    'D1 SODA 3',
    'D2 LEMONADE 3',
    'D3 TEA 2',
    'D4 WATER 0',
    'A1 POTATO_CAKES 7',
    'A2 SPINACH_DIP 5',
    'A3 OYSTERS 13',
    'A4 CHEESE_FRIES 4',
    'A5 ONION_RINGS 7',
    'S1 COBB 14',
    'S2 CAESAR 13',
    'S3 GREEK 12',
    'E1 BURGER 16',
    'E2 PASTA 15',
    'E3 GNOCCHI 14',
    'E4 GRILLED_STEAK_SANDWICH 17',
    'T1 CARAMEL_CHEESECAKE 13',
    'T2 APPLE_COBBLER 12',
    'T3 BROWNIE_SUNDAE 9',
    'T4 FLAN 8'
]

drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items = ['T1', 'T2',  'T3', 'T4']

def create_menu():
    menu_dict_list = []
    for item in menu_items:
        code, name, price = item.split()
        price = int(price)
        if code not in drink_items:  # Non-drink items get random stock
            stock = random.randint(25, 50)
        else:
            stock = 100  # Unlimited drinks stock
        menu_dict_list.append({"code": code, "name": name, "price": price, "stock": stock})
    return menu_dict_list

menu = create_menu()
for item in menu:
    print(item)

def update_menu(menu, code, new_name=None, new_price=None):
    for item in menu:
        if item['code'] == code:
            if new_name:
                item['name'] = new_name
            if new_price:
                item['price'] = new_price
            print(f"Updated item: {item}")
            return
    print(f"Item with code {code} not found.")


def add_item(menu, code, name, price, stock):
    menu.append({"code": code, "name": name, "price": price, "stock": stock})
    print(f"Added new item: {code} - {name}")


def remove_item(menu, code):
    menu[:] = [item for item in menu if item['code'] != code]
    print(f"Removed item with code {code}")

def take_order(menu, code, quantity):
    quantity = int(quantity)
    for item in menu:
        if item['code'] == code:
            if item['stock'] >= quantity:
                item['stock'] -= quantity
                print(f"Order successful for {quantity} {item['name']}(s). Remaining stock: {item['stock']}")
            else:
                print(f"Not enough stock for {item['name']}. Available stock: {item['stock']}")
            return
    print(f"Item with code {code} not found.")


def display_menu(menu):
    print("\nCurrent Menu:")
    for item in menu:
        print(f"{item['code']}: {item['name']} - ${item['price']} | Stock: {item['stock']}")
    print("\n")

