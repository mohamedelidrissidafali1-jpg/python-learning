# Number list analyzer
print("=== Number List Analyzer ===\n")

numbers = []

# Get numbers
print("Enter numbers (type 'done' to finish):")
while True:
    user_input = input("Number: ")
    
    if user_input.lower() == "done":
        break
    
    numbers.append(int(user_input))

if len(numbers) == 0:
    print("No numbers entered!")
else:
    print(f"\nYour numbers: {numbers}")
    
    # Basic stats
    print("\n--- Statistics ---")
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    
    # Even vs Odd
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print(f"\nEven numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    
    # Positive vs Negative
    positive = [num for num in numbers if num > 0]
    negative = [num for num in numbers if num < 0]
    zero = [num for num in numbers if num == 0]
    
    print(f"\nPositive: {len(positive)}")
    print(f"Negative: {len(negative)}")
    print(f"Zero: {len(zero)}")
    prime_numbers = []
    for num in numbers:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
            
    unique_numbers = set(numbers)
    print(unique_numbers)





