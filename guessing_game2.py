from random import *

def playerStats(firstName):
    print(f"Hello, {firstName}. Good morning!")

def gQuestion(firstName):
    print(f"Would you like to play a game {firstName} \n ")

def convert_to_bool(answer):
    if answer.lower() == 'yes':
        return True
    elif answer.lower() == 'no':
        return False
    else:
        return "Invalid input. Please enter 'yes' or 'no'."

def win(trys):
    print(f"You won after {trys}.")

def playGame(ToF):
    if ToF == True:
        print(f"Pick a number between 1 and 100, {name}\n")
    else:
        exit()

def gameCheck(guess):
    if x == guess:
        return "Winner"
    else:
        return "Try again"

name = input("First name: \n")

# Call functions 
playerStats(name)
gQuestion(name)
response = input("Yes or No:")
boolean_response = convert_to_bool(response)
print(boolean_response)
playGame(boolean_response)
userNum = int(input())
game_result = gameCheck(userNum)
print(game_result)

x = randint(1, 100)
print(x)
