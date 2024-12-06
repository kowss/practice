#Guess the numbers between 1 and 100

import random

def game():
    val=random.randint(1,100)
    while True:
        num=int(input("Enter random numbers between 1 and 100:"))
        if num == val:
            print("Correct answer")
            break
        elif num > val:
            print("Enter lesser number")
        elif num < val:
            print("Enter greater number")

game()

while True:
    user_input=input("Do you want to continue (yes/no):").strip().lower()
    if user_input == "yes":
        game()
    elif user_input == "no":
        print("Finish the game")
        break
    else:
        print("Invalid input")
        