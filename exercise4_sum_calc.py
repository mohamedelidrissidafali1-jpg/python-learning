# Sum calculator - add numbers until user wants to stop
print("=== Sum Calculator ===\n")

total = 0
count = 0
largest = None
smallest = None
positive_count = 0
negative_count = 0

while True:
    # FIX: strip() removes spaces, lower() ignores case
    user_input = input("Enter a number (or 'done' to finish): ").strip().lower()

    if user_input == "done":
        break

    # error handling for invalid input
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
        continue

    # track largest and smallest
    if largest is None:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    # count positives and negatives
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

    # update total and count
    total += number
    count += 1

    print(f"Running total: {total}")

# results
if count > 0:
    average = total / count
    print("\n--- Results ---")
    print(f"Total numbers entered: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")
else:
    print("No numbers entered.")

