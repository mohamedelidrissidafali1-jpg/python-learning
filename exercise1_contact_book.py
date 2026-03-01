# Contact book with dictionaries and functions
print("=== Contact Book ===\n")

contacts = {}

def add_contact(name, phone, email):
    if name in contacts:
        print("Contact already exists")
        return 
    else:
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


def edit_contact(name):
    if name in contacts:
        new_phone = input("New phone :  ")
        new_email = input("New email :  ")
        contacts[name]["phone"] = new_phone
        contacts[name]["email"] = new_email
        print(f"✓ Updated contact: {name}")
    else:
        print(f"{name} not found!")

def count_contacts():
    return len(contacts)

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
    print("5. Edit contact")
    print("6. Count contacts")
    print("7. Exit")
    
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
        name = input("Enter contact name to edit: ")
        edit_contact(name)

    elif choice == "6":
        print(count_contacts())

    
    elif choice == "7":
        print("Goodbye!")
        break