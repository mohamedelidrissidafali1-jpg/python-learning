import random

playing = True

while playing:

    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100")

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

        if too_low_count + too_high_count == 3:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is even!")
            else:
                print("💡 Hint: The number is odd!")

        if attempts == max_attempts:
            print(f"\n😞 Game over! The number was {secret_number}")

    # play again question
    answer = input("\nDo you want to play again? (yes/no): ").lower()

    if answer == "no":
        playing = False

print("Thanks for playing! 👋")


    


