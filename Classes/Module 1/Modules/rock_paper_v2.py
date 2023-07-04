import random
import time

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
    print("\nPreparing the game...")
    show_loading_screen()
    print("\nPlayer's choice:")
    print(get_hand_art(player_choice))

    print("Computer is choosing...")
    show_loading_screen()
    
    computer_choice = random.choice(choices)

    print("Computer's choice:")
    print(get_hand_art(computer_choice))

    print("\nCalculating the result...")
    show_loading_screen()

    if player_choice == computer_choice:
        print("It's a tie!")
        return 1
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
        return 2
    else:
        print("Computer wins!")
        return 0

def get_hand_art(choice):
    if choice == "Rock":
        return rock
    elif choice == "Paper":
        return paper
    elif choice == "Scissors":
        return scissors

def show_loading_screen():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(char, end="\r")
            time.sleep(0.1)
    print(" ", end="\r")

# Main game loop
player_points = 0
computer_points = 0

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
        result = play_game(player_choice)

        if result == 1:
            print("It's a tie! No points awarded.")
        elif result == 2:
            player_points += 1
            print("You win this round! You earn 1 point.")
        else:
            computer_points += 1
            print("Computer wins this round! It earns 1 point.")

        print("Player points:", player_points)
        print("Computer points:", computer_points)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from 0 to 3.")

    print("\n---\n")
