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

def calculate_total_value():
    total = 0
    for product, info in inventory.items():
        total += info["price"] * info["quantity"]
    return total

def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty!")
        return
    
    print("\n--- Inventory ---")
    for name, info in inventory.items():
        value = info["price"] * info["quantity"]
        print(f"{name}:")
        print(f"  Price: ${info['price']}")
        print(f"  Quantity: {info['quantity']}")
        print(f"  Total Value: ${value}")

# Test the system
add_product("Laptop", 1000, 5)
add_product("Mouse", 25, 20)
add_product("Keyboard", 75, 15)

display_inventory()

update_quantity("Mouse", 10)  # Add 10 more
update_quantity("Laptop", -2)  # Sell 2

print(f"\nTotal inventory value: ${calculate_total_value()}")

