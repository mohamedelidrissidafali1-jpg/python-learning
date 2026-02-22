# Dictionaries - key-value pairs
print("=== Dictionaries Basics ===\n")

# Creating dictionaries
person = {
    "name": "Ahmed",
    "age": 25,
    "city": "Cairo",
    "is_student": True
}

print(person)

# Accessing values by key
print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")

# Using .get() (safer - doesn't crash if key missing)
print(f"City: {person.get('city')}")
print(f"Country: {person.get('country', 'Not found')}")  # Default value

# Adding/modifying
person["country"] = "Egypt"  # Add new key
person["age"] = 26  # Modify existing

print(f"\nUpdated: {person}")

# Removing items
person.pop("is_student")  # Remove specific key
print(f"After removing: {person}")

# Checking if key exists
if "name" in person:
    print("\nName key exists!")

# Dictionary methods
print(f"\nKeys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Looping through dictionary
print("\n--- Loop through dictionary ---")
for key in person:
    print(f"{key}: {person[key]}")

# Better way - using items()
print("\n--- Using items() ---")
for key, value in person.items():
    print(f"{key}: {value}")

# Nested dictionaries
students = {
    "student1": {"name": "Ali", "grade": 85},
    "student2": {"name": "Sara", "grade": 92},
    "student3": {"name": "Omar", "grade": 78}
}

print(f"\n{students}")
print(f"Sara's grade: {students['student2']['grade']}")