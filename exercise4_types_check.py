# Check types of different values

# Create different variables
name = "Ahmed"
age = 25
height = 1.75
is_student = True
score = 100

# Check their types
print("=== Type Checking ===")
print(f"name = '{name}' is type: {type(name)}")
print(f"age = {age} is type: {type(age)}")
print(f"height = {height} is type: {type(height)}")
print(f"is_student = {is_student} is type: {type(is_student)}")
print(f"score = {score} is type: {type(score)}")

# What about calculations?
print("\n=== Type of Calculations ===")
result1 = 10 + 5
result2 = 10 / 5
result3 = 10 // 5
result4 = "Hello" + " World"

print(f"10 + 5 = {result1}, type: {type(result1)}")
print(f"10 / 5 = {result2}, type: {type(result2)}")
print(f"10 // 5 = {result3}, type: {type(result3)}")
print(f"'Hello' + ' World' = '{result4}', type: {type(result4)}")