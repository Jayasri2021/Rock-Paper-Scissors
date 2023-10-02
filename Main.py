import random


def RPS():
    options = ["ROCK", "PAPER", "SCISSORS"]

    while True:
        input_choice = input(
            "Enter rock, paper, or scissors (or 'Q' to quit): "
        ).upper()
        if input_choice == "Q":
            print("Thanks for playing!")
            break
        elif input_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        comp_choice = random.choice(options)
        print("Computer's choice:", comp_choice)

        if input_choice == comp_choice:
            print("It's a tie!")
        elif (
            (input_choice == "ROCK" and comp_choice == "SCISSORS")
            or (input_choice == "PAPER" and comp_choice == "ROCK")
            or (input_choice == "SCISSORS" and comp_choice == "PAPER")
        ):
            print("You win!")
        else:
            print("You lose!")


RPS()
