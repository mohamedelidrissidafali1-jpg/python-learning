# Functions - reusable code blocks
print("=== Functions ===\n")

# Basic function (no parameters, no return)
def greet():
    print("Hello, World!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ahmed")
greet_person("Sara")

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)

# Function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"\nResult: {result}")

# Using return value in expression
total = multiply(3, 7) + multiply(2, 4)
print(f"Total: {total}")

# Default parameters
def greet_with_title(name, title="Mr"):
    print(f"Hello, {title} {name}")

greet_with_title("Ahmed")  # Uses default "Mr"
greet_with_title("Sara", "Ms")  # Custom title

# Return multiple values
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    return total, average, maximum

nums = [10, 20, 30, 40, 50]
sum_val, avg_val, max_val = get_stats(nums)

print(f"\nSum: {sum_val}")
print(f"Average: {avg_val}")
print(f"Maximum: {max_val}")

# Function with list parameter
def print_list(items):
    for item in items:
        print(f"- {item}")

fruits = ["apple", "banana", "orange"]
print("\nFruits:")
print_list(fruits)

# Function with dictionary parameter
def print_person(person_dict):
    print(f"Name: {person_dict['name']}")
    print(f"Age: {person_dict['age']}")

person = {"name": "Ahmed", "age": 25}
print("\nPerson info:")
print_person(person)