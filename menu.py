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

# Function to create the menu list of dictionaries
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
    print(item)T