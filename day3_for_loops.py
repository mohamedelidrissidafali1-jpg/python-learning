# For loops - repeating actions
print("=== Basic For Loop ===\n")

# Loop 5 times
for i in range(5):
    print(f"Loop number: {i}")

print("\n=== Understanding range() ===\n")

# range(5) gives: 0, 1, 2, 3, 4 (starts at 0!)
for i in range(5):
    print(i)

# range(start, stop)
print("\nFrom 1 to 5:")
for i in range(1, 6):  # 6 is NOT included
    print(i)

# range(start, stop, step)
print("\nEven numbers 0 to 10:")
for i in range(0, 11, 2):  # step by 2
    print(i)

print("\nCountdown from 10:")
for i in range(10, 0, -1):  # negative step
    print(i)
print("Blast off!")

# Using the loop variable
print("\n=== Multiplication Table ===")
number = 5
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# Nested loops (loop inside loop)
print("\n=== Nested Loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")