import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock , paper , scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("your input is rock")
            print("Computer input is scissors")
            print("You win!")
            user_input += 1
        else:
            print("Your input is rock")
            print("Computer input is Paper")
            print("Computer Win!")
            computer_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("your input is paper")
            print("Computer input is scissors")
            print("Computer win!")
            computer_input += 1
        else:
            print("Your input is paper")
            print("Computer input is rock")
            print("You Win!")
            user_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It's a tie!")
        elif computer_input == "rock":
            print("your input is scissors")
            print("Computer input is rock")
            print("You win!")
            user_input += 1
        else:
            print("Your input is scissors")
            print("Computer input is paper")
            print("Computer Win!")
            computer_points += 1

    else:
        print("Enter from the given options which are rock , paper and scissors")





