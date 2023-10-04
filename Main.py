import random


def RPS():
    options = ["rock", "paper", "scissors"]

    while True:
        input_choice = input(
            "Enter rock, paper, or scissors (or 'q' to quit): "
        ).lower()
        if input_choice == "q":
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
            (input_choice == "rock" and comp_choice == "scissors")
            or (input_choice == "paper" and comp_choice == "rock")
            or (input_choice == "scissors" and comp_choice == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")


RPS()
