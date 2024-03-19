# New rock paper scissors project
"""
 In this game, the user gets the first chance to pick the option between Rock, paper, and scissors.
 After the computer select from the remaining two choices(randomly), the winner is decided as per the rules.
"""

# I would firstly ask both users how many rounds they wish to play
x = 0
rounds = int(input("How many rounds of the game ? "))
maxPoint = int(input("What is the max point of the game? "))

while x != rounds:
    print(" Pick a choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    choice = int(input("Enter your choice"))

    # now we have to make sure user can only enter number of range 1 - 3
    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors"))

