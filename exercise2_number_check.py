# Number checker - even/odd, positive/negative
print("=== Number Checker ===\n")

number = int(input("Enter a number: "))

# Check even or odd
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# Check positive, negative, or zero
if number > 0:
    print(f"{number} is POSITIVE")
elif number < 0:
    print(f"{number} is NEGATIVE")
else:
    print(f"{number} is ZERO")

# Check if divisible by 3
if number % 3 == 0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is NOT divisible by 3")

# Check if divisible by 5
if number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is NOT divisible by 5")

# Check range
if number >= 1 and number <= 10:
    print(f"{number} is between 1 and 10")
elif number >= 11 and number <= 100:
    print(f"{number} is between 11 and 100")
elif number >= 50 and number <= 100:
    print(f"{number} is between 50 and 100")
else:
    print(f"{number} is outside the range 1-100")
