from random import *

def playerStats(firstName):
    print(f"Hello, {firstName}. Good morning!")

def gQuestion(firstName):
    print(f"Would you like to play a game {firstName}? \n ")

def convert_to_bool(answer):
    if answer.lower() == 'yes':
        return True
    elif answer.lower() == 'no':
        return False
    else:
        return "Invalid input. Please enter 'yes' or 'no'."

def win(trys):
    print(f"You won after {trys} attempts.")

def playGame(ToF):
    if ToF == True:
        print(f"Pick a number between 1 and 100, {name}\n")
    else:
        exit()

def gameCheck(guess, x):
    if x == guess:
        return "Winner"
    elif x > guess:
        return "Too low! Try again"
    else:
        return "Too high! Try again"

name = input("First name: \n")

# Call functions 
playerStats(name)
gQuestion(name)
response = input("Yes or No:")
boolean_response = convert_to_bool(response)
print(boolean_response)

if boolean_response == True:
    x = randint(1, 100)    # Pick a random number between 1 and 100.
    guess_count = 0
    while True:
        playGame(boolean_response)
        userNum = int(input())
        guess_count += 1
        game_result = gameCheck(userNum, x)
        print(game_result)
        if game_result == "Winner":
            win(guess_count)
            break