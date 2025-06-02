import random

def number_guessing_game():
    print("-----Welcome to the Number Guessing Game!-----")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess == number_to_guess:
                print("Congratulations! You guessed the number correctly!")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            attempts -= 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == 0:
        print(f"\n You've run out of attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()
