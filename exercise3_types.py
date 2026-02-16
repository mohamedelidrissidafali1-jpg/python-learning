# Understanding data types and conversion

# 1. String to Number
age_as_text = "20"
height_as_text = "1.75"

print(f"age_as_text = {age_as_text}, type: {type(age_as_text)}")
print(f"height_as_text = {height_as_text}, type: {type(height_as_text)}")

# Convert to numbers
age = int(age_as_text)
height = float(height_as_text)

print(f"\nAfter conversion:")
print(f"age = {age}, type: {type(age)}")
print(f"height = {height}, type: {type(height)}")

# Now we can do math
print(f"\nMath with converted values:")
print(f"In 10 years: {age + 10}")
print(f"Double height: {height * 2}")

# 2. Number to String
score = 100
score_string = str(score)
print(f"\nscore = {score}, type: {type(score)}")
print(f"score_string = {score_string}, type: {type(score_string)}")

# 3. Boolean values
is_student = True
is_working = False

print(f"\nis_student = {is_student}, type: {type(is_student)}")
print(f"is_working = {is_working}, type: {type(is_working)}")

# Try this - what happens?
# Uncomment the line below to see the error
# result = "25" + 5  # This will cause an error!
# print(result)

# The correct way:
result = int("25") + 5
print(f"\nCorrect way: int('25') + 5 = {result}")

age_as_text = "100"

age = int(age_as_text)
print(f"50 years ago my age was {age - 50}")


is_working = True 

is_student = False 

print(f"str(True) = {str(True)}, type: {type(str(True))}")
print(f"int(True) = {int(True)}, type: {type(int(True))}")

