# Interactive age calculator
print("=== Age Calculator ===\n")

birth_year = int(input("What year were you born? "))
current_year = 2026

age = current_year - birth_year

# Check impossible age
if age < 0:
    print("Error! You haven't been born yet!")
    exit()

# Current age
print(f"\nYou are {age} years old in 2026")

# Future ages (moved here - more logical order)
print(f"\n--- Your Future Ages ---")
print(f"In 2030 you will be {2030 - birth_year} years old")
print(f"In 2040 you will be {2040 - birth_year} years old")
print(f"In 2050 you will be {2050 - birth_year} years old")

# Adult check
if age >= 18:
    print("\nYou are an adult")
    years_adult = age - 18
    print(f"You've been an adult for {years_adult} years")
else:
    print("\nYou are a minor")
    years_until_adult = 18 - age
    print(f"You'll be an adult in {years_until_adult} years")

# Age category
if age >= 65:
    print("You are a senior citizen")
elif age >= 18:
    print("You are a working-age adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Future calculation
years_ahead = int(input("\nHow many years in the future? "))
future_age = age + years_ahead
print(f"In {years_ahead} years, you'll be {future_age} years old")


