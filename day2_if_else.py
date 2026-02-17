# If/Else statements - making decisions!
print("=== If/Else Demo ===\n")

# Basic if statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
    print("You can vote!")

# If/else
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If/elif/else (multiple conditions)
score = int(input("\nEnter your test score (0-100): "))

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Acceptable")
elif score >= 60:
    print("Grade: D - Need improvement")
else:
    print("Grade: F - Failed")

# Multiple conditions with 'and'
age = int(input("\nEnter age again: "))
has_license = input("Do you have a license? (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You can drive!")
else:
    print("You cannot drive yet")

# Multiple conditions with 'or'
day = input("\nWhat day is it? ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")