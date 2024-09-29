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

def process_customer_request(menu, code, quantity):
    quantity = int(quantity)
    for item in menu:
        if item['code'] == code:
            if item['stock'] >= quantity:
                item['stock'] -= quantity
                print(f"Order successful for {quantity} {item['name']}(s). Remaining stock: {item['stock']}")
                return True
            else:
                print(f"Not enough stock for {item['name']}. Available stock: {item['stock']}")
                return False
    print(f"Item with code {code} not found.")
    return False

def display_menu(menu):
    print("\nCurrent Menu:")
    for item in menu:
        print(f"{item['code']}: {item['name']} - ${item['price']} | Stock: {item['stock']}")
    print("\n")