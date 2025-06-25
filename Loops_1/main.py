# Guessing Game Using Loops
import random

no_of_turns = 10
lucky_num = random.randint(1, 100)

while no_of_turns >= 0:
    user_input = int(input(f"Can you guess a number"))
    if user_input == lucky_num:
        print("You've won the game")
        break
    elif user_input > lucky_num:
        print("To High!!!")
        no_of_turns -= 1
        print(f"You've Got {no_of_turns} turn left to win the game")
    elif user_input < lucky_num:
        print("To Low!!!")
        no_of_turns -= 1
        print(f"You've Got {no_of_turns} turn left to win the game")
    else:
        print("You guessed a wrong number higher that the value")
        no_of_turns -= 1

    if no_of_turns == 0:
        print(f"The correct number is {lucky_num}")
        break
