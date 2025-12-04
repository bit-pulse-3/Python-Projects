import random

choice = input("To start press Y anything else to exit:")
while choice == "y" or choice == "Y":
    game_list = ["S", "R", "P"]
    count = 3
    user_points = 0
    comp_points = 0
    while count != 0:
        computer_choice = random.randint(0, 2)
        comp_choicestr = game_list[computer_choice]
        user_choice = input("Choose again:\nR.Rock\nP.Paper\nS.Scissors").upper()
        if user_choice not in game_list:
            print("Invalid Option..")
            continue
        print(user_choice)
        if user_choice == "S" and comp_choicestr == "P":
            user_points += 1
            count -= 1
        elif user_choice == "R" and comp_choicestr == "S":
            user_points += 1
            count -= 1
        elif user_choice == "P" and comp_choicestr == "R":
            user_points += 1
            count -= 1
        elif user_choice == "P" and comp_choicestr == "S":
            comp_points += 1
            count -= 1
        elif user_choice == "R" and comp_choicestr == "P":
            comp_points += 1
            count -= 1
        elif user_choice == "S" and comp_choicestr == "R":
            comp_points += 1
            count -= 1
        else:
            print("Same thing through...")

    if user_points >= 2:
        print("You won the game.")
    else:
        print("Computer Won.")

    choice = input("Do you want to play again(Y/N):")
