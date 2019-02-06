import random

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a ramdom play to the computer
computer = t[random.randint(0, 2)]

# set player to false
player = False

while player == False:
    # set player to True
    player = input("Rocker, Paper, Scissors?: ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", computer, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play. Please check your spelling.")

    player = False
    computer = t[random.randint(0, 2)]
