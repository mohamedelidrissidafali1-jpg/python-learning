# Contact book with dictionaries and functions
print("=== Contact Book ===\n")

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"✓ Added contact: {name}")

def view_all_contacts():
    if len(contacts) == 0:
        print("No contacts yet!")
        return
    
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"{name}:")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")

def search_contact(name):
    if name in contacts:
        info = contacts[name]
        print(f"\n{name}:")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
    else:
        print(f"\n{name} not found!")

def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"✓ Deleted: {name}")
    else:
        print(f"{name} not found!")

# Menu system
while True:
    print("\n--- Menu ---")
    print("1. Add contact")
    print("2. View all")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    
    elif choice == "2":
        view_all_contacts()
    
    elif choice == "3":
        name = input("Search name: ")
        search_contact(name)
    
    elif choice == "4":
        name = input("Delete name: ")
        delete_contact(name)
    
    elif choice == "5":
        print("Goodbye!")
        break