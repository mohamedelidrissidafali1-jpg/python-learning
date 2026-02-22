# Combining dictionaries and functions
print("=== Student Management System ===\n")

# List of student dictionaries
students = []

def add_student(name, age, grade):
    """Add a new student to the system"""
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print(f"✓ Added student: {name}")

def display_all_students():
    """Display all students"""
    if len(students) == 0:
        print("No students yet!")
        return
    
    print("\n--- All Students ---")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} - Age: {student['age']}, Grade: {student['grade']}")

def find_student(name):
    """Find a student by name"""
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

def calculate_average():
    """Calculate average grade"""
    if len(students) == 0:
        return 0
    
    total = sum(student['grade'] for student in students)
    return total / len(students)

# Using the functions
add_student("Ahmed", 20, 85)
add_student("Sara", 22, 92)
add_student("Omar", 21, 78)

display_all_students()

# Find specific student
search_name = "Sara"
found = find_student(search_name)
if found:
    print(f"\nFound: {found['name']} has grade {found['grade']}")
else:
    print(f"\n{search_name} not found")

# Calculate average
avg = calculate_average()
print(f"\nClass average: {avg:.2f}")