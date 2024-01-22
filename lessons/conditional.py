"""Demonstrate"""

user_input:str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# 

if user_number < 10:
    print("small")
else:
    print("big")
    
print(user_input)