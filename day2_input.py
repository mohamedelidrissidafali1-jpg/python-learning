# Taking input from users
print("=== User Input Demo ===\n")

# Basic input - EVERYTHING from input() is a STRING
name = input("What is your name? ")
print(f"Hello, {name}!")

# Notice: input() always returns a STRING
age_text = input("How old are you? ")
print(f"You entered: {age_text}")
print(f"Type of age_text: {type(age_text)}")

# To do math, we need to convert to int
age = int(age_text)
print(f"Type after conversion: {type(age)}")
print(f"Next year you'll be {age + 1} years old")

# We can convert in one line
height = float(input("What is your height in meters? "))
print(f"Your height is {height}m")

# Multiple inputs
city = input("Which city do you live in? ")
favorite_color = input("What's your favorite color? ")

print(f"\n--- Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"City: {city}")
print(f"Favorite color: {favorite_color}")