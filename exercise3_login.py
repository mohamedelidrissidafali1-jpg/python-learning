# Simple login system
print("=== Login System ===\n")

# Correct credentials (hardcoded for now)
correct_username = "Mohamed"
correct_password = "200602"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")


if len(password) < 5:
    print("your password is too short")
    exit()

# Check credentials
if username == correct_username and password == correct_password:
    print("\n✓ Login successful!")
    print("Welcome to the system!")
else:
    print("\n✗ Login failed!")
    
    # Give specific error
    if username != correct_username:
        print("Error: Incorrect username")
    if password != correct_password:
        print("Error: Incorrect password")