import random

Welcome = ("Welcome to a match of Rock, Paper, and Scissors\n"
           "Please Input 0 for rock, 1 for scissors and 2 for paper: \n")

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

ASCII = [Rock, Paper, Scissors]
options = ["Rock", "Paper", "Scissors"]

def play_round():
    user_input = int(input(Welcome))
    user_choice = options[user_input]
    computer_input = random.randint(0, 2)
    computer_choice = options[computer_input]

    print("You chose:", user_choice)
    print(ASCII[user_input])

    print("Computer chose:", computer_choice)
    print(ASCII[computer_input])

    return user_input, computer_input

def determine_winner(user_input, computer_input):
    if user_input == computer_input:
        return "draw"
    elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 0):
        return "user"
    else:
        return "computer"

def race_to_three():
    computer_wins = 0
    user_wins = 0

    while computer_wins < 3 and user_wins < 3:
        user_input, computer_input = play_round()
        winner = determine_winner(user_input, computer_input)

        if winner == "user":
            user_wins += 1
            print("You win this round!\n")
        elif winner == "computer":
            computer_wins += 1
            print("Computer wins this round!\n")
        else:
            print("It's a draw!\n")

        print(f"Score: You {user_wins} - {computer_wins} Computer\n")

    if user_wins == 3:
        print("Congratulations! You won the match!")
    else:
        print("Computer wins the match! Better luck next time!")

race_to_three()
