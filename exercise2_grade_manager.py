# Student grade manager with CSV
import csv
import os

GRADES_FILE = "grades.csv"

def initialize_file():
    """Create file with headers if it doesn't exist"""
    if not os.path.exists(GRADES_FILE):
        with open(GRADES_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Math", "Science", "English", "Average"])

def add_student(name, math, science, english):
    """Add a student with grades"""
    try:
        average = (math + science + english) / 3
        
        with open(GRADES_FILE, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, math, science, english, f"{average:.2f}"])
        
        print(f"✓ Added {name}")
    except Exception as e:
        print(f"Error adding student: {e}")

def view_all_students():
    """Display all students"""
    if not os.path.exists(GRADES_FILE):
        print("No students yet!")
        return
    
    try:
        with open(GRADES_FILE, "r") as file:
            reader = csv.reader(file)
            print("\n--- All Students ---")
            for row in reader:
                print(f"{row[0]:<15} Math: {row[1]:<5} Science: {row[2]:<5} English: {row[3]:<5} Avg: {row[4]}")
    except Exception as e:
        print(f"Error reading file: {e}")

def calculate_class_average():
    """Calculate class average"""
    if not os.path.exists(GRADES_FILE):
        print("No data yet!")
        return
    
    try:
        with open(GRADES_FILE, "r") as file:
            reader = csv.DictReader(file)
            averages = []
            for row in reader:
                averages.append(float(row["Average"]))
        
        if len(averages) == 0:
            print("No students yet!")
        else:
            class_avg = sum(averages) / len(averages)
            print(f"\nClass Average: {class_avg:.2f}")
    except Exception as e:
        print(f"Error calculating average: {e}")

def find_top_student():
    """Find student with highest average"""
    if not os.path.exists(GRADES_FILE):
        print("No data yet!")
        return
    
    try:
        with open(GRADES_FILE, "r") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            
            if len(students) == 0:
                print("No students yet!")
                return
            
            top_student = max(students, key=lambda x: float(x["Average"]))
            print(f"\nTop Student: {top_student['Name']} with average {top_student['Average']}")
    except Exception as e:
        print(f"Error finding top student: {e}")

def search_student(name):
    if not os.path.exists(GRADES_FILE): 
        print("No data yet!")
        return

    found = False

    with open(GRADES_FILE, "r") as file: 
        reader = csv.reader(file)

        next( reader )

        for row in reader:
            if row[0] == name:
                print(f"Name: {row[0]} | Math: {row[1]} | Science: {row[2]} | English: {row[3]} | Avg: {row[4]}")
                found = True

    if not found:
        print("Student not found.")

def show_failing_students():

    if not os.path.exists(GRADES_FILE):
        print("No data yet!")
        return

    with open(GRADES_FILE, "r") as file:
        reader = csv.reader(file)

        next(reader) 

        found = False

        for row in reader:
            if float(row[4]) < 60: 
                print(f"{row[0]} is failing with average {row[4]}")
                found = True

        if not found:
            print("No failing students 🎉")
def show_top_students():
    """Display top 3 students and write them to top_students.csv"""
    if not os.path.exists(GRADES_FILE):
        print("No data yet!")
        return

    try:
        students = []
        with open(GRADES_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        if not students:
            print("No students yet!")
            return

        students.sort(key=lambda x: float(x["Average"]), reverse=True)
        top_students = students[0:3]

        print("\n--- Top Students ---")
        for s in top_students:
            print(f"{s['Name']}: Avg {s['Average']}")

        with open("top_students.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Math", "Science", "English", "Average"])
            writer.writeheader()
            for student in top_students:
                writer.writerow(student)
    except Exception as e:
        print(f"Error writing top students to file: {e}")
        
def show_top_students():
    """Display top 3 students and write them to top_students.csv"""
    if not os.path.exists(GRADES_FILE):
            print("No data yet!")
            return

    try:
        students = []
        with open(GRADES_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        if not students:
            print("No students yet!")
            return

        students.sort(key=lambda x: float(x["Average"]), reverse=True)
        top_students = students[0:3]

        print("\n--- Top Students ---")
        for s in top_students:
            print(f"{s['Name']}: Avg {s['Average']}")

        with open("top_students.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Math", "Science", "English", "Average"])
            writer.writeheader()
            for student in top_students:
                writer.writerow(student)
    except Exception as e:
        print(f"Error showing top students: {e}")

def delete_student(name):
    """Delete a student by name"""
    if not os.path.exists(GRADES_FILE):
        print("No data yet!")
        return

    try:
        students = []
        with open(GRADES_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row)

        header = students[0]
        students = students[1:]

        students = [s for s in students if s[0] != name]

        with open(GRADES_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(students)

        print(f"✓ Deleted {name}")
    except Exception as e:
        print(f"Error deleting student: {e}")

# Initialize file
initialize_file()

# Main menu
while True:
    print("\n=== Grade Manager ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Class average")
    print("4. Top student")
    print("5. Search student")
    print("6. Show failing students")
    print("7. Show top students")
    print("8. Delete student")
    print("9. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        try:
            name = input("Student name: ")
            math = int(input("Math grade: "))
            science = int(input("Science grade: "))
            english = int(input("English grade: "))
            add_student(name, math, science, english)
        except ValueError:
            print("Invalid grade! Must be a number.")
    
    elif choice == "2":
        view_all_students()
    
    elif choice == "3":
        calculate_class_average()
    
    elif choice == "4":
        find_top_student()
    
    elif choice == "5":
        name = input("Enter student name to search: ")
        search_student(name)
    
    elif choice == "6": 
        show_failing_students()
    
    elif choice == "7":
        show_top_students()
    
    elif choice == "8":
        name = input("Enter student name to delete: ")
        delete_student(name)
    
    elif choice == "9":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")