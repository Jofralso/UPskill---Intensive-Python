
import random

# ASCII art representations of Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Choices available in the game
choices = ["Rock", "Paper", "Scissors"]

# Game logic
def play_game(player_choice):
    computer_choice = random.choice(choices)

    print("\nPlayer's choice:")
    print(get_hand_art(player_choice))

    print("Computer's choice:")
    print(get_hand_art(computer_choice))

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

def get_hand_art(choice):
    if choice == "Rock":
        return rock
    elif choice == "Paper":
        return paper
    elif choice == "Scissors":
        return scissors

# Main game loop
while True:
    print("Let's play Rock Paper Scissors!")
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Quit")

    player_input = input("Enter your choice (0-3): ")

    if player_input == "0":
        print("Thanks for playing!")
        break

    try:
        player_choice = choices[int(player_input) - 1]
        play_game(player_choice)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from 0 to 3.")

    print("\n---\n")
