# Number guessing game
import random  # This lets us generate random numbers

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
too_high_count = 0
too_low_count = 0


while attempts < max_attempts:
    attempts += 1
    
    guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Your guess: "))
    
    if guess == secret_number:
        print(f"🎉 Correct! You won in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try higher.")
        too_low_count += 1

    else:
        print("Too high! Try lower.")
        too_high_count += 1

    
    if attempts == max_attempts:
        print(f"\n😞 Game over! The number was {secret_number}")