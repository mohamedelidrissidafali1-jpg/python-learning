# Product inventory system
print("=== Product Inventory ===\n")

inventory = {}

def add_product(name, price, quantity):
    inventory[name] = {
        "price": price,
        "quantity": quantity
    }
    print(f"✓ Added: {name}")

def update_quantity(name, amount):
    if name in inventory:
        inventory[name]["quantity"] += amount
        print(f"✓ Updated {name}: {inventory[name]['quantity']} in stock")
    else:
        print(f"{name} not found!")

def remove_product(name):
    if name in inventory:
        del inventory[name] 
        print(f"✓ deleted: {name}") 
    else:
        print(f"{name} not found!")

def search_product(name):
    if name in inventory:
       info = inventory[name]
       print(f"{name}:")
       print(f"  Price: ${info['price']}")
       print(f"  Quantity: {info['quantity']}")
    else:  
       print(f"{name} not found!")

def calculate_total_value():
    total = 0
    for product, info in inventory.items():
        total += info["price"] * info["quantity"]
        if info["quantity"] < 5 :
            print("⚠ Low stock!")
    return total

def display_inventory():
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\n--- Inventory ---")
    for name, info in inventory.items():
        value = info["price"] * info["quantity"]
        print(f"{name}:")
        print(f"  Price: ${info['price']}")
        print(f"  Quantity: {info['quantity']}")
        print(f"  Total Value: ${value}")

def sell_product(name, quantity):
    if name in inventory:
        if quantity > inventory[name]["quantity"]: 
            print("Not enough stock!")
        else:
            inventory[name]["quantity"] -= quantity
            revenue = inventory[name]["price"] * quantity
            print(f"Sold {quantity} {name}(s) for ${revenue}") 
    else:
        print(f"{name} not found!")
# Test the system
add_product("Laptop", 1000, 5)
add_product("Mouse", 25, 20)
add_product("Keyboard", 75, 15)

display_inventory()

update_quantity("Mouse", 10)  # Add 10 more
update_quantity("Laptop", -2)  # Sell 2

print(f"\nTotal inventory value: ${calculate_total_value()}")

