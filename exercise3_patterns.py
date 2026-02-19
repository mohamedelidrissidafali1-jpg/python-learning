# Pattern printer
print("=== Pattern Printer ===\n")

size = int(input("Enter size: "))


# Pattern 1: Triangle
print("Triangle:")
for i in range(1, size + 1):

    print("*" * i)

# Pattern 2: Square
print("\nSquare:")
size = int(input("Enter size: "))
for i in range(size):
    print("*" * size)

# Pattern 3: Pyramid
print("\nPyramid:")
height = size
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


print("\nInverted Triangle:")
for i in range(size):
    print("*" * i)

for i in range(1, size + 1):
    print(str(i) * i)
