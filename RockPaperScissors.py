import random
# New rock paper scissors project
"""
 In this game, the user gets the first chance to pick the option between Rock, paper, and scissors.
 After the computer select from the remaining two choices(randomly), the winner is decided as per the rules.
"""

# I would firstly ask both users how many rounds they wish to play
x = 0
y = 0
userPoint = 0
compPoint = 0
rounds = int(input("How many rounds of the game ? "))
maxPoint = int(input("What is the max point of the game? "))

while x != rounds or y != maxPoint:
    print(" Pick a choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    choice = int(input("Enter your choice "))

    # now we have to make sure user can only enter number of range 1 - 3
    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors"))

    if choice == 1:
        choiceName = "Rock"
    elif choice == 2:
        choiceName = "Paper"
    else:
        choiceName = "Scissors"

    print("User has selected ", choiceName)

    # Since only two users which is one user and the computer gets to choose randomly between 1,2,3
    print("Now the computer has to make a selection")

    # we give the computer a choice of picking between 3 random integers
    choiceCom = random.randint(1,3)

    # in rock paper scissors game both players cannot have the same value , so we make sure to avoid that
    while choiceCom == choice:
        choiceCom = random.randint(1, 3)

    if choiceCom == 1:
        choiceNameCom = "Rock"
    elif choiceCom == 2:
        choiceNameCom = "Paper"
    else:
        choiceNameCom = "Scissors"

    print("Computer has selected ", choiceNameCom)
    # conditions for winning the game
    if (choice == 1 and choiceCom == 2) or (choice == 2 and choiceCom == 3) or (choice == 3 and choiceCom == 1):
        compPoint += 1
        print("Computer wins!")
    elif (choice == 1 and choiceCom == 3) or (choice == 2 and choiceCom == 1) or (choice == 3 and choiceCom == 2):
        userPoint += 1
        print("User wins!")
    else:
        print("It's a draw!")

    if userPoint == maxPoint or compPoint == maxPoint:
        print("You have reached the maximum point possible")
        break

    print("The user point is ", userPoint)
    print("The Computer point is ", compPoint)

    x = x + 1
    y = y + 2

print("Thanks for playing")

