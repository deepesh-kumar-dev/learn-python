import random
print("Guess a number between 1 and 100 in your head, then press Enter to see if I guessed it right!")

def guess_game():
    is_guessed = False
    range_start = 1
    range_end = 100
    while not is_guessed:
        random_number = random.randint(range_start, range_end)
        user_input = input(f"Is your number {random_number}? (correct/c, higher/h, lower/l): ")
        if user_input.lower() == "correct" or user_input.lower() == "c":
            print("Yay! I guessed it right!")
            is_guessed = True
        elif user_input.lower() == "higher" or user_input.lower() == "h":
            range_start = random_number + 1
            print("Okay, I'll guess higher next time!")
        elif user_input.lower() == "lower" or user_input.lower() == "l":
            range_end = random_number - 1
            print("Okay, I'll guess lower next time!")
        else:
            print("Please enter 'correct/c', 'higher/h', or 'lower/l'.")

guess_game()