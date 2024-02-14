"""EX03"""
__author__: str = "730720425"

import random

def input_guess(grid_size: int, specification: str) -> int:
    GRID_SIZE = grid_size
    assert specification == "row" or specification == "column"
    if specification == "row":
        guess_row: int = int(input("Guess a row: "))
        while guess_row > GRID_SIZE or guess_row <= 0:
            guess_row = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
        return guess_row
    else:
        guess_column: int = int(input("Guess a column: "))
        while guess_column > GRID_SIZE or guess_column <= 0:
            guess_column = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
        return guess_column
    
def print_grid(grid_size: int, guess_row: int, guess_column: int, t_f: bool) -> None:
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    row_counter: int = 1
    if t_f == True:
        result = RED_BOX
    else:
        result = WHITE_BOX
    while row_counter <= grid_size:
        storage: str = ""
        column_counter: int = 1
        if guess_row == row_counter:
            while column_counter <= grid_size:
                if guess_column == column_counter:
                    storage = storage + result
                else:
                    storage = storage + BLUE_BOX
                column_counter = column_counter + 1
        else:
            while column_counter <= grid_size:
                storage = storage + BLUE_BOX
                column_counter = column_counter + 1
        print(storage)
        row_counter = row_counter + 1

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column:int) -> bool:
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False
    
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    turns: int = 1
    while turns <= 5:
        print(f"=== Turn {turns}/5 ===")
        guess_row = input_guess(grid_size, "row")
        guess_column = input_guess(grid_size, "column")
        correctness: bool = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(grid_size, guess_row, guess_column, correctness)
        if correctness == True:
            print("Hit!")
            print(f"You won in {turns}/5 turns!")
            turns += 100
        else:
            print("Miss!")
            turns += 1
    if turns == 6:
        print("X/5 - Better luck next time!")

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
