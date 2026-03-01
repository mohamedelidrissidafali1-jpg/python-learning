# Working with CSV files
import csv

print("=== CSV Files ===\n")

# Writing CSV
print("Writing CSV file")
students = [
    ["Name", "Age", "Grade"],
    ["Ahmed", 20, 85],
    ["Sara", 22, 92],
    ["Omar", 21, 78]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("✓ Wrote students.csv")

# Reading CSV
print("\nReading CSV file")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV into dictionary
print("\nReading CSV as dictionary")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']}: Grade {row['Grade']}")

# Writing dictionary to CSV
print("\nWriting dictionary to CSV")
students_dict = [
    {"name": "Ali", "age": 23, "grade": 88},
    {"name": "Layla", "age": 24, "grade": 95}
]

with open("students2.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write column names
    writer.writerows(students_dict)
print("✓ Wrote students2.csv")