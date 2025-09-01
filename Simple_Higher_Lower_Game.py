# Import the libraries
import random
import art
import game_data

# Keep track of already used choices so they don't repeat
done_list = []

# Function to make a random choice from remaining items
def make_choice():
    # Build a list of available items (excluding already used ones)
    available_choices = [item for item in game_data.data if item not in done_list]
    
    if not available_choices:   # If no items left, stop the game gracefully
        return None
    
    # Randomly select one item from the available list
    choice = random.choice(available_choices)
    
    # Add the selected item to the used list so it won't appear again
    done_list.append(choice)
    return choice


# Variables for the game
choice1 = None
choice2 = None
a_or_b = ""            # Stores the correct answer ("a" or "b")
correct_choice = None  # Tracks the winner of the round
user_score = 0         # Keeps the player's score
should_continue = True # Controls whether the game keeps running


# Game loop
while should_continue:
    print(art.logo)  # Print the game logo (ASCII art)

    # Get the first choice
    choice1 = make_choice()
    if choice1 is None:   # If no choices left, end the game
        print("No more choices available. Game over!")
        break

    correct_choice = choice1

    # Get the second choice
    choice2 = make_choice()
    if choice2 is None:   # If only one choice left, end the game
        print("No more choices available. Game over!")
        break

    # Main comparison loop
    while True:
        # Show the two options
        print(f"Compare A: {correct_choice['name']}, a {correct_choice['description']}, from {correct_choice['country']}.")
        print(art.vs)
        print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")

        # Decide which option has more followers
        if choice2['follower_count'] > choice1['follower_count']:
            a_or_b = "b"             # Correct answer is B
            correct_choice = choice2 # Winner becomes the "correct choice"
        else:
            a_or_b = "a"             # Correct answer is A
            # Here, correct_choice is already choice1

        # Ask the player for their guess
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Handle invalid inputs → keep asking until valid ("a" or "b")
        while user_input not in ["a", "b"]:
            print("Invalid input! Please type only 'A' or 'B'.")
            user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if the guess is correct
        if user_input != a_or_b:
            # Wrong guess → game over
            print(f"Sorry, that's wrong. Final score: {user_score}\n\n")
            should_continue = False  # End outer loop
            break
        else:
            # Correct guess → increase score and continue
            user_score += 1
            print(f"You're right! Current score: {user_score}\n")

            # The winner (correct choice) becomes new "A"
            choice1 = correct_choice
            # Get a new "B"
            choice2 = make_choice()
            
            if choice2 is None:   # If no more choices left, stop game
                print("No more choices available. Game over!")
                should_continue = False
                break
