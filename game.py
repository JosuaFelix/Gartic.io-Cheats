import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10

print("Welcome to the Guessing Game!")
print(f"Guess the secret number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number ({secret_number}) in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# If the player runs out of attempts
if attempts >= max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}. Try again next time!")
