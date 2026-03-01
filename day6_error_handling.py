# Error handling - try/except
print("=== Error Handling ===\n")

# Without error handling - this crashes!
# number = int("hello")  # Uncomment to see the error

# With error handling
print("Example 1: Basic try/except")
try:
    number = int("hello")
    print(f"Number: {number}")
except:
    print("Error: Could not convert to number!")

# Specific error types
print("\nExample 2: Specific error types")
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: That's not a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Catching the error message
print("\nExample 3: Getting error details")
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Index out of range
except IndexError as e:
    print(f"Error: {e}")

# Multiple operations with error handling
print("\nExample 4: Multiple operations")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age: {age}")
except ValueError as e:
    print(f"Invalid input: {e}")

# try/except/else/finally
print("\nExample 5: else and finally")
try:
    x = int(input("Enter a number: "))
    result = 100 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid number!")
else:
    # Runs if NO error occurred
    print(f"Result: {result}")
finally:
    # ALWAYS runs, error or not
    print("Operation completed")

# Real-world example: Safe user input
def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

print("\nExample 6: Safe input function")
age = get_number("Enter your age: ")
print(f"Your age is: {age}")

