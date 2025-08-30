# ------------------------------
# Simple Blackjack Game in Python
# ------------------------------

import random

# Define the card deck (11 represents Ace, 10 is repeated for J, Q, K)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Lists to hold the cards of player and dealer
my_cards = []
dealer_cards = []

# Functions to distribute cards
def distribute_me():
    """Add a random card to the player's hand."""
    my_cards.append(random.choice(cards))

def distribute_dealer():
    """Add a random card to the dealer's hand."""
    dealer_cards.append(random.choice(cards))

# Control flags for game flow
game = True
another_game = True
new_game = True

# Main game loop
while game:
    # Start a new game by dealing 2 cards to both player and dealer
    while new_game:
        print("\nWelcome to the Game of BlackJack. Remember '21'!")
        distribute_me()
        distribute_me()
        distribute_dealer()
        distribute_dealer()
        break  # Break ensures we only initialize once per game

    # Show player's cards and dealer's first card
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}\n")

    # Player decision loop
    while another_game:
        another_card = input("Type 'y' to get another card, type 'n' to pass:")

        if another_card == "y":
            # Player takes another card
            distribute_me()
            distribute_dealer()  # Dealer also gets a card in this version
            print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
            print(f"Computer's first card: [{dealer_cards[0]}]")

            # If player score exceeds 21 -> Bust
            if sum(my_cards) > 21:
                print("Bust! You Lose")
                my_cards = []
                dealer_cards = []
                break
            continue

        elif another_card == "n":
            # Dealer keeps drawing cards until total is at least 17
            while sum(dealer_cards) < 17:
                distribute_dealer()

            # Final hands
            print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n")

            # Game results
            if sum(dealer_cards) > 21:
                print("Dealer loses! You Win")
            elif sum(my_cards) == sum(dealer_cards):
                print("Draw Game")
            elif sum(my_cards) > sum(dealer_cards):
                print("You Win!")
            elif sum(my_cards) < sum(dealer_cards):
                print("Sorry, dealer Wins!")

            # Reset cards for next round
            my_cards = []
            dealer_cards = []

            # Ask player if they want to play again
            play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if play == "n":
                game = False
            elif play == "y":
                break  # Restart the loop for a new game
        break
