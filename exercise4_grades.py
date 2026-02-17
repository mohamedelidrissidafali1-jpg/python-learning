# Grade calculator
print("=== Grade Calculator ===\n")

# Get scores
print("Enter your scores (0-100):")
math_score = int(input("Math: "))
science_score = int(input("Science: "))
english_score = int(input("English: "))

# Calculate average
average = (math_score + science_score + english_score) / 3
print(f"\nYour average score: {average:.2f}")  # .2f = 2 decimal places

# Determine grade
if average >= 90:
    grade = "A"
    message = "Excellent!"
elif average >= 80:
    grade = "B"
    message = "Good job!"
elif average >= 70:
    grade = "C"
    message = "Acceptable"
elif average >= 60:
    grade = "D"
    message = "Need improvement"
else:
    grade = "F"
    message = "Failed - study harder!"

print(f"Grade: {grade}")
print(f"Message: {message}")

# Check if passed
if average >= 60:
    print("\n✓ You PASSED!")
else:
    print("\n✗ You FAILED")
    points_needed = 60 - average
    print(f"You need {points_needed:.2f} more points to pass")