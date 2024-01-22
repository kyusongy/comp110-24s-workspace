"""Practice with variable and input functions."""

first_name: str = input("What is your name?")
fave_number_str: str = input("What is your favourite number?")
fave_number: int = int(fave_number_str)
higher_number:int = fave_number + 1


print("Hello " + first_name + "!")
print("My favourite number is "+ str(higher_number))