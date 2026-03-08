import random

def get_choices():
    player_choice = input("Enter a choice (stone, paper, scissor): ")
    options = ["stone", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_winner(player, computer):
    if (player == computer):
        return "Match Draw!"

    if (player == "stone"):
        if (computer == "paper"):
            return "Computer Won!"
        if (computer == "scissor"):
            return "You Won!"

    if (player == "paper"):
        if (computer == "stone"):
            return "You Won!"
        if (computer == "scissor"):
            return "Computer Won!"

    if (player == "scissors"):
        if (computer == "stone"):
            return "Computer Won!"
        if (computer == "paper"):
            return "You Won!"

    return "Invalid Input!"

choices = get_choices()
player = choices["player"]
computer = choices["computer"]

print(f"You chose {player}, computer chose {computer}.")
print(check_winner(player, computer))