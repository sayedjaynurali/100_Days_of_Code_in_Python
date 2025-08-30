import random  # Import the random module to generate random numbers

def game():
    # Introductory messages for the player
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Dictionary to store the randomly generated number and the player's last guess
    guess = {"random_number": random.randint(1, 100), "last_guess": None}
    
    # Dictionary to store the attempt count (based on difficulty level)
    attempt = {"level": None}
    
    # DEBUG (optional) → prints the random number so you can test easily
    # Remove this line for actual gameplay
    print(guess)

    # Ask user to choose difficulty
    set_level = input("Choose your level 'easy' or 'hard': ")

    # Based on chosen level, set number of attempts
    if set_level == "hard":
        attempt["level"] = 5
    elif set_level == "easy":
        attempt["level"] = 10
    
    # Main game loop → runs until attempts run out OR user guesses correctly
    while attempt["level"] > 0 and guess["last_guess"] != guess["random_number"]:
        # Show remaining attempts
        print(f"You have {attempt['level']} attempts remaining to guess the number.")
        
        # Take player's guess (convert input to integer)
        try:
            this_guess = int(input("Make a guess: "))
        except ValueError:
            # Handle invalid input (like letters instead of numbers)
            print("Invalid input! Please enter a number between 1 and 100.")
            continue  # Skip this loop iteration without losing attempts

        # Store the latest guess
        guess["last_guess"] = this_guess

        # Check guess against the random number
        if this_guess == guess["random_number"]:
            print(f"You Guessed the right number 🎉 The number was {guess['random_number']}.")
        elif this_guess < guess["random_number"]:
            attempt["level"] -= 1
            print("Too Low.")
        elif this_guess > guess["random_number"]:
            attempt["level"] -= 1
            print("Too High.") 

        # If no attempts left, end the game
        if attempt["level"] == 0 and guess["last_guess"] != guess["random_number"]:
            print("You have run out of attempts 😢 Please re-run the game to play again.")      

# Run the game function
game()
