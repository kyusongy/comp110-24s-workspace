"""Nbr Guessing Game"""
from random import randint

SECRET: int = randint(1,5)

correct: bool = False

while correct ==False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        correct = True
    else:
        if guess < SECRET:
            print("The guess is too low! Guess again!")
        else:
            print("The guess is too high! Guess again!")