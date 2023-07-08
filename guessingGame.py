from random import *

x = randint(1, 100)  
print(x)

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
        print(f"pick a number {name}\n")
    else:
        exit()
def gameCheck(guess):
    if x == guess:
        return "winner"
    else:
        return "try again"
name = input("firstName: \n")

# call functions 
playerStats(name)
gQuestion(name)
response = input("Yes or No:")
boolean_response = convert_to_bool(response)
print(boolean_response)
playGame(boolean_response)
userNum = int(input())
gameCheck(userNum)
print(userNum)


