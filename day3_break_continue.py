# Break and Continue
print("=== Break - Exit loop early ===\n")

# Find first number divisible by 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"First number divisible by 7: {i}")
        break  # Stop the loop immediately

print("\n=== Continue - Skip to next iteration ===\n")

# Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:  # if even
        continue  # Skip the rest, go to next i
    print(f"Odd number: {i}")

print("\n=== Real example: Password attempts ===")

max_attempts = 3
correct_password = "secret"

for attempt in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt}/{max_attempts} - Enter password: ")
    
    if password == correct_password:
        print("✓ Access granted!")
        break  # Exit loop on success
    else:
        if attempt < max_attempts:
            print("✗ Wrong password, try again")
        else:
            print("✗ Maximum attempts reached. Locked out!")