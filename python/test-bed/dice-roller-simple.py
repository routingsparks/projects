import random


def main():
    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dice ...")
        print("The values are ...")
        print(random.randint(min, max))

        roll_again = input("Roll the dices again?: ")
        if roll_again == "no" or roll_again == "n":
            print("Okay, thank you for playing.")
            exit(1)

        if __name__ == '__main__':
            main()


main()
