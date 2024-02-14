"""EX02_ One Shot Battleship."""
__author__ = "730720425"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
row_counter: int = 1

GRID_SIZE: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

guess_row: int = int(input("Guess a row: "))
while guess_row > GRID_SIZE or guess_row <= 0:
    guess_row = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
guess_column: int = int(input("Guess a column: "))
while guess_column > GRID_SIZE or guess_column <= 0:
    guess_column = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))

if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    result = RED_BOX
else:
    result = WHITE_BOX

while row_counter <= GRID_SIZE:
    storage: str = ""
    column_counter: int = 1
    if guess_row == row_counter:
        while column_counter <= GRID_SIZE:
            if guess_column == column_counter:
                storage = storage + result
            else:
                storage = storage + BLUE_BOX
            column_counter = column_counter + 1
    else:
        while column_counter <= GRID_SIZE:
            storage = storage + BLUE_BOX
            column_counter = column_counter + 1
    print(storage)
    row_counter = row_counter + 1


if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    print("Hit!")
elif guess_row == SECRET_ROW and guess_column != SECRET_COLUMN:
    print("Close! Correct row, wrong column.")
elif guess_column == SECRET_COLUMN and guess_row != SECRET_ROW:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")