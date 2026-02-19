# Multiplication table generator
print("=== Multiplication Table Generator ===\n")

number = int(input("Enter a number: "))
limit = int(input("How many multiples? "))

print(f"\nMultiplication table for {number}:")
for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")