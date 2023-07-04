import random
import time

# ASCII art representations of hands
rock_frames = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)
      (_____)
      (_____)
   \\  (____)
---.__(___)
''',
    '''
    _______
---'   ____)
      (_____)
      (_____)
   \\  (____)
    \\__(___)
'''
]

paper_frames = [
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
    ________)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
 __________)
'''
]

scissors_frames = [
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---._____)__
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

# Choices available in the game
choices = ["Rock", "Paper", "Scissors"]

# Characters' attributes
player1 = {
    "name": "Player 1",
    "health": 100,
    "attack": 15,
    "defense": 5
}

player2 = {
    "name": "Player 2",
    "health": 100,
    "attack": 15,
    "defense": 5
}

# Game logic
def player_attack(player, opponent, player_choice):
    opponent_choice = random.choice(choices)

    print(f"\n{player['name']}'s choice:")
    animate_hand(player_choice)

    print(f"{opponent['name']}'s choice:")
    animate_hand(opponent_choice)

    if player_choice == opponent_choice:
        print("It's a tie! No damage is dealt.")
    elif (
        (player_choice == "Rock" and opponent_choice == "Scissors")
        or (player_choice == "Paper" and opponent_choice == "Rock")
        or (player_choice == "Scissors" and opponent_choice == "Paper")
    ):
        opponent_damage = max(0, player["attack"] - opponent["defense"])
        opponent["health"] -= opponent_damage
        print(f"{player['name']} wins! {opponent['name']} receives {opponent_damage} damage.")
    else:
        player_damage = max(0, opponent["attack"] - player["defense"])
        player["health"] -= player_damage
        print(f"{opponent['name']} wins! {player['name']} receives {player_damage} damage.")

def animate_hand(hand_frames):
    for frame in hand_frames:
        print("\033c")  # Clear the console screen
        print(frame)
        time.sleep(0.5)

# PvP mode
def pvp_mode():
    while True:
        print("Player 1's Turn:")
        print(f"\n{player1['name']}'s Health: {player1['health']}")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player1_input = input("Enter your choice (1-3): ")

        if player1_input not in ["1", "2", "3"]:
            print("Invalid input. Please enter a number from 1 to 3.")
            continue

        player1_choice = choices[int(player1_input) - 1]

        print("\nPlayer 2's Turn:")
        print(f"\n{player2['name']}'s Health: {player2['health']}")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player2_input = input("Enter your choice (1-3): ")

        if player2_input not in ["1", "2", "3"]:
            print("Invalid input. Please enter a number from 1 to 3.")
            continue

        player2_choice = choices[int(player2_input) - 1]

        player_attack(player1, player2, player1_choice)
        player_attack(player2, player1, player2_choice)

        if player1["health"] <= 0:
            print(f"{player1['name']} has been defeated. {player2['name']} wins!")
            break

        if player2["health"] <= 0:
            print(f"{player2['name']} has been defeated. {player1['name']} wins!")
            break

        print("\n---\n")
        time.sleep(1)  # Delay between each round

# Main game loop
while True:
    print("Welcome to Rock Paper Scissors!")

    print("\nGame Modes:")
    print("1. Player vs. Player")
    print("2. Quit")
    mode_input = input("Enter your choice (1-2): ")

    if mode_input not in ["1", "2"]:
        print("Invalid input. Please enter 1 or 2.")
        continue

    mode = int(mode_input)

    if mode == 1:
        print("\nStarting Player vs. Player Mode...")
        pvp_mode()
    else:
        print("\nExiting the game. Goodbye!")
        break
