# Multiplication table generator
print("=== Multiplication Table Generator ===\n")

number = int(input("Enter a number: "))
limit = int(input("How many multiples? "))

print(f"\nMultiplication table for {number}:")

total = 0  # for Task 3 (sum of results)

# Task 2 → reverse order loop
for i in range(limit, 0, -1):
    result = number * i
    total = total + result
    print(f"{number} x {i} = {result}")

# Task 3 → show total
print(f"\nTotal of results = {total}")
