# Grade tracker
print("=== Grade Tracker ===\n")

grades = []

# Get grades
while True:
    grade_input = input("Enter grade (or 'done' to finish): ")
    
    if grade_input.lower() == "done":
        break
    
    grade = float(grade_input)
    
    if 0 <= grade <= 100:
        grades.append(grade)
        print(f"✓ Added grade: {grade}")
    else:
        print("Grade must be between 0 and 100!")

if len(grades) == 0:
    print("No grades entered!")
else:
    # Calculate statistics
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print("\n--- Statistics ---")
    print(f"All grades: {grades}")
    print(f"Number of grades: {len(grades)}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    
    # Count passing grades
    passing = 0
    for grade in grades:
        if grade >= 60:
            passing += 1
    
    print(f"Passing grades (≥60): {passing}")
    print(f"Failing grades (<60): {len(grades) - passing}")