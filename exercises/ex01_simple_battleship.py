"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730720425"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
storage: str = ""

player_choice_input: str = input("Pick a secret boat location between 1 and 4:")
player_choice: int = int(player_choice_input)
if player_choice < 1:
    print(f"Error! {player_choice} too low!")
    exit()
if player_choice > 4:
    print(f"Error! {player_choice} too high!")
    exit()

player_guess_input: str = input("Pick a secret boat location between 1 and 4:")
player_guess: int = int(player_guess_input)
if player_guess < 1:
    print(f"Error! {player_guess} too low!")
    exit()
if player_guess > 4:
    print(f"Error! {player_guess} too high!")
    exit()




if player_choice == player_guess:
    result = RED_BOX
else:
    result = WHITE_BOX


if player_guess == 1:
    storage = result + BLUE_BOX + BLUE_BOX + BLUE_BOX
if player_guess == 2:
    storage = BLUE_BOX + result + BLUE_BOX + BLUE_BOX
if player_guess == 3:
    storage = BLUE_BOX + BLUE_BOX + result + BLUE_BOX
if player_guess == 4:
    storage = BLUE_BOX + BLUE_BOX + BLUE_BOX + result

if player_choice == player_guess:
    print(storage)
    print("Correct! You hit the ship.")
else:
    print(storage)
    print("Incorrect! You missed the ship.")